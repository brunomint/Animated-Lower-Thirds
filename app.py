#!/usr/bin/env python3
"""
Servidor Flask para Animated Lower Thirds
Permite controle remoto via rede de qualquer dispositivo
"""

from flask import Flask, render_template, send_from_directory, request, jsonify, make_response
from flask_socketio import SocketIO, emit, join_room, leave_room
import os
import socket
import qrcode
from io import BytesIO
import base64
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lower-thirds-secret-key-2024'

# Configurar SocketIO para comunicação em tempo real
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    """Obtém o IP local da máquina"""
    try:
        # Conecta a um endereço externo para descobrir o IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def generate_qr_code(url):
    """Gera QR Code para acesso rápido via mobile"""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Rotas principais
@app.route('/')
def index():
    """Página inicial com links para controle e browser source"""
    local_ip = get_local_ip()
    port = request.environ.get('SERVER_PORT', '5000')
    
    control_url = f"http://{local_ip}:{port}/control"
    source_url = f"http://{local_ip}:{port}/source"
    
    qr_control = generate_qr_code(control_url)
    qr_source = generate_qr_code(source_url)
    
    return render_template('index.html', 
                         local_ip=local_ip, 
                         port=port,
                         control_url=control_url,
                         source_url=source_url,
                         qr_control=qr_control,
                         qr_source=qr_source)

@app.route('/control')
def control_panel():
    """Painel de controle - mantém o arquivo original"""
    return render_template('control-panel.html')

@app.route('/source')
def browser_source():
    """Browser source para OBS - mantém o arquivo original"""
    print("🎬 Servindo browser-source.html")
    response = make_response(render_template('browser-source.html'))
    # Headers para evitar cache
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/debug/source')
def debug_source():
    """Debug da rota source"""
    return jsonify({
        'template': 'browser-source.html',
        'route': '/source',
        'message': 'Esta é a rota correta do browser source'
    })

@app.route('/test_lower_third')
def test_lower_third():
    """Página de teste para verificar se Lower Thirds aparecem"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Teste Lower Third</title>
        <style>
            body { background: #000; color: #fff; font-family: Arial; }
            .test-box { 
                background: red; 
                color: white; 
                padding: 20px; 
                margin: 20px;
                border-radius: 10px;
            }
            iframe { 
                width: 100%; 
                height: 400px; 
                border: 2px solid #fff;
                background: #333;
            }
        </style>
    </head>
    <body>
        <div class="test-box">
            <h1>🎬 Teste Lower Third</h1>
            <p>Se você vê esta mensagem, o servidor está funcionando!</p>
            <p><strong>IP do servidor:</strong> 192.168.0.19:5000</p>
        </div>
        
        <div class="test-box">
            <h2>Browser Source (deve mostrar Lower Thirds):</h2>
            <iframe src="/source"></iframe>
        </div>
        
        <div class="test-box">
            <h2>Painel de Controle:</h2>
            <p><a href="/control" style="color: #4facfe;">Abrir Painel de Controle</a></p>
        </div>
    </body>
    </html>
    '''

@app.route('/debug/routes')
def debug_routes():
    """Lista todas as rotas disponíveis"""
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'rule': rule.rule
        })
    
    return jsonify({
        'total_routes': len(routes),
        'routes': sorted(routes, key=lambda x: x['rule']),
        'server_ip': '192.168.0.19:5000'
    })

@app.route('/test_websocket')
def test_websocket():
    """Página de teste para WebSocket"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Teste WebSocket</title>
        <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
        <style>
            body { font-family: Arial; padding: 20px; background: #000; color: #fff; }
            .status { padding: 10px; margin: 10px 0; border-radius: 5px; }
            .connected { background: #4caf50; }
            .disconnected { background: #f44336; }
            .message { background: #2196f3; }
            button { padding: 10px 20px; margin: 5px; font-size: 16px; }
            #log { background: #333; padding: 10px; height: 300px; overflow-y: scroll; }
        </style>
    </head>
    <body>
        <h1>🔌 Teste WebSocket Lower Thirds</h1>
        
        <div id="status" class="status disconnected">❌ Desconectado</div>
        
        <button onclick="testConnection()">🔄 Testar Conexão</button>
        <button onclick="sendTestCommand()">📤 Enviar Comando Teste</button>
        <button onclick="clearLog()">🗑️ Limpar Log</button>
        
        <h3>📋 Log de Eventos:</h3>
        <div id="log"></div>
        
        <script>
            const socket = io();
            const statusDiv = document.getElementById('status');
            const logDiv = document.getElementById('log');
            
            function addLog(message) {
                const time = new Date().toLocaleTimeString();
                logDiv.innerHTML += `<div>[${time}] ${message}</div>`;
                logDiv.scrollTop = logDiv.scrollHeight;
            }
            
            socket.on('connect', function() {
                statusDiv.innerHTML = '✅ Conectado (ID: ' + socket.id + ')';
                statusDiv.className = 'status connected';
                addLog('🔌 Conectado ao WebSocket');
            });
            
            socket.on('disconnect', function() {
                statusDiv.innerHTML = '❌ Desconectado';
                statusDiv.className = 'status disconnected';
                addLog('🔌 Desconectado do WebSocket');
            });
            
            socket.on('connected', function(data) {
                addLog('📨 Recebido evento connected: ' + JSON.stringify(data));
            });
            
            socket.on('lower_thirds_update', function(data) {
                addLog('🎬 Recebido lower_thirds_update: ' + JSON.stringify(data));
            });
            
            function testConnection() {
                addLog('🔄 Testando conexão...');
                if (socket.connected) {
                    addLog('✅ WebSocket está conectado');
                } else {
                    addLog('❌ WebSocket não está conectado');
                    socket.connect();
                }
            }
            
            function sendTestCommand() {
                const testData = {
                    alt_1_name: 'TESTE WEBSOCKET',
                    alt_1_info: 'Funcionando!',
                    alt_1_switch: true,
                    global_animation_time: 1000
                };
                
                socket.emit('lower_thirds_command', testData);
                addLog('📤 Enviado comando teste: ' + JSON.stringify(testData));
            }
            
            function clearLog() {
                logDiv.innerHTML = '';
            }
            
            addLog('🚀 Página carregada, iniciando WebSocket...');
        </script>
    </body>
    </html>
    '''

# Servir arquivos estáticos
@app.route('/common/<path:filename>')
def serve_static(filename):
    """Serve arquivos estáticos (CSS, JS, etc.)"""
    return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)

@app.route('/logos/<path:filename>')
def serve_logos(filename):
    """Serve logos da pasta static/logos"""
    logos_path = os.path.join(BASE_DIR, 'static', 'logos')
    
    # Criar pasta logos se não existir
    if not os.path.exists(logos_path):
        os.makedirs(logos_path)
    
    # Verificar se arquivo existe
    file_path = os.path.join(logos_path, filename)
    if os.path.exists(file_path):
        return send_from_directory(logos_path, filename)
    else:
        # Retornar imagem padrão transparente se não encontrar
        print(f"❌ Logo não encontrado: {filename}")
        return '', 404

@app.route('/upload_logo', methods=['POST'])
def upload_logo():
    """Upload de logo para o servidor"""
    try:
        if 'logo' not in request.files:
            return jsonify({'status': 'error', 'message': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['logo']
        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'Nenhum arquivo selecionado'}), 400
        
        # Verificar se é uma imagem
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'}
        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            return jsonify({'status': 'error', 'message': 'Formato de arquivo não suportado'}), 400
        
        # Criar pasta logos se não existir
        logos_path = os.path.join(BASE_DIR, 'static', 'logos')
        if not os.path.exists(logos_path):
            os.makedirs(logos_path)
        
        # Salvar arquivo
        filename = file.filename
        file_path = os.path.join(logos_path, filename)
        file.save(file_path)
        
        print(f"✅ Logo salvo: {filename}")
        return jsonify({
            'status': 'success', 
            'message': 'Logo enviado com sucesso',
            'filename': filename,
            'url': f'/logos/{filename}'
        })
        
    except Exception as e:
        print(f"❌ Erro no upload: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/logos')
def list_logos():
    """Lista todos os logos disponíveis"""
    try:
        logos_path = os.path.join(BASE_DIR, 'static', 'logos')
        
        if not os.path.exists(logos_path):
            os.makedirs(logos_path)
            return jsonify({'logos': []})
        
        logos = []
        for filename in os.listdir(logos_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
                logos.append({
                    'filename': filename,
                    'url': f'/logos/{filename}'
                })
        
        return jsonify({'logos': logos})
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API para comunicação entre controle e source
@app.route('/api/broadcast', methods=['POST'])
def broadcast_message():
    """API para enviar mensagens via WebSocket"""
    try:
        data = request.get_json()
        if data:
            # Emite mensagem para todos os clientes conectados
            socketio.emit('lower_thirds_update', data, broadcast=True)
            return jsonify({'status': 'success', 'message': 'Broadcast sent'})
        else:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# WebSocket events
@socketio.on('connect')
def handle_connect():
    """Cliente conectado"""
    client_ip = request.environ.get('REMOTE_ADDR', 'unknown')
    print(f'🔌 Cliente WebSocket conectado: {request.sid} (IP: {client_ip})')
    emit('connected', {'data': 'Conectado ao servidor Lower Thirds', 'sid': request.sid})

@socketio.on('disconnect')
def handle_disconnect():
    """Cliente desconectado"""
    print(f'Cliente desconectado: {request.sid}')

@socketio.on('lower_thirds_command')
def handle_lower_thirds_command(data):
    """Recebe comandos do painel de controle e retransmite para o browser source"""
    print(f'🎮 Comando recebido do controle: {data}')
    print(f'📡 Retransmitindo para browser source...')
    # Retransmite para todos os clientes (especialmente o browser source)
    emit('lower_thirds_update', data, broadcast=True, include_self=False)
    print(f'✅ Comando retransmitido com sucesso')

@socketio.on('join_room')
def handle_join_room(data):
    """Permite que clientes entrem em salas específicas"""
    room = data.get('room', 'default')
    join_room(room)
    emit('room_joined', {'room': room})

@socketio.on('leave_room')
def handle_leave_room(data):
    """Permite que clientes saiam de salas específicas"""
    room = data.get('room', 'default')
    leave_room(room)
    emit('room_left', {'room': room})

if __name__ == '__main__':
    # Configurações do servidor
    host = '0.0.0.0'  # Permite acesso de qualquer IP da rede
    port = 5000
    debug = True
    
    local_ip = get_local_ip()
    
    print("=" * 60)
    print("🎬 ANIMATED LOWER THIRDS - SERVIDOR FLASK")
    print("=" * 60)
    print(f"🌐 Servidor iniciado em: http://{local_ip}:{port}")
    print(f"🎮 Painel de Controle: http://{local_ip}:{port}/control")
    print(f"📺 Browser Source (OBS): http://{local_ip}:{port}/source")
    print("=" * 60)
    print("📱 Use o QR Code na página inicial para acesso rápido via mobile")
    print("🔗 Acesse de qualquer dispositivo na mesma rede WiFi")
    print("=" * 60)
    
    try:
        socketio.run(app, host=host, port=port, debug=debug, allow_unsafe_werkzeug=True)
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        print("💡 Tente usar uma porta diferente ou verifique se a porta está livre")
