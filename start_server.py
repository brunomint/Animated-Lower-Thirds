#!/usr/bin/env python3
"""
Script de inicialização para o Animated Lower Thirds
Instala dependências automaticamente e inicia o servidor
"""

import subprocess
import sys
import os
import importlib.util

def check_and_install_requirements():
    """Verifica e instala dependências automaticamente"""
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    if not os.path.exists(requirements_file):
        print("❌ Arquivo requirements.txt não encontrado!")
        return False
    
    print("🔍 Verificando dependências...")
    
    # Lista de pacotes necessários
    required_packages = [
        'flask',
        'flask_socketio',
        'qrcode',
        'pillow',
        'eventlet'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        if importlib.util.find_spec(package.replace('-', '_')) is None:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"📦 Instalando dependências: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', requirements_file
            ])
            print("✅ Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar dependências: {e}")
            return False
    else:
        print("✅ Todas as dependências já estão instaladas!")
    
    return True

def start_server():
    """Inicia o servidor Flask"""
    try:
        from app import app, socketio
        print("🚀 Iniciando servidor...")
        socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
    except ImportError as e:
        print(f"❌ Erro ao importar aplicação: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🎬 ANIMATED LOWER THIRDS - INICIALIZADOR")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('app.py'):
        print("❌ Arquivo app.py não encontrado!")
        print("💡 Execute este script no diretório do projeto")
        sys.exit(1)
    
    # Instalar dependências se necessário
    if not check_and_install_requirements():
        print("❌ Falha ao instalar dependências")
        sys.exit(1)
    
    # Iniciar servidor
    start_server()

if __name__ == '__main__':
    main()
