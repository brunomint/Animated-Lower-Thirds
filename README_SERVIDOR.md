# 🎬 Animated Lower Thirds - Servidor Flask

Este projeto é um fork do [Animated Lower Thirds](https://github.com/noeal-dac/Animated-Lower-Thirds) original criado por **noeal-dac**, com adição de servidor Flask para controle remoto via rede de qualquer dispositivo.

> **📋 Veja também**: [README_FORK.md](README_FORK.md) para comparação completa com o projeto original.

## 🚀 Início Rápido

### Opção 1: Inicialização Automática (Recomendada)
```bash
python start_server.py
```

### Opção 2: Inicialização Manual
```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar servidor
python app.py
```

## 📱 Como Usar

### 1. **Acesso Local**
- Abra seu navegador em: `http://localhost:5000`
- Você verá uma página com QR Codes e links diretos

### 2. **Controle Remoto**
- **Painel de Controle**: `http://SEU_IP:5000/control`
- **Browser Source (OBS)**: `http://SEU_IP:5000/source`
- **QR Code**: Escaneie com o celular para acesso rápido

### 3. **Configuração no OBS**
1. Adicione uma fonte **"Browser"**
2. Use a URL: `http://SEU_IP:5000/source`
3. Defina resolução: 1920x1080
4. Configure FPS: 30

## 🌐 Funcionalidades

### ✅ **Controle via Rede**
- Controle de qualquer dispositivo na mesma WiFi
- Sincronização em tempo real via WebSocket
- Interface responsiva para mobile e desktop

### ✅ **Compatibilidade Total**
- Mantém todos os arquivos originais
- Funciona com configurações existentes
- Suporte a hotkeys e shortcuts

### ✅ **Recursos Avançados**
- QR Code para acesso rápido
- Detecção automática de IP local
- Interface moderna e intuitiva
- Comunicação bidirecional em tempo real

## 🔧 Configuração Avançada

### Alterar Porta
Edite o arquivo `app.py` na linha:
```python
port = 5000  # Altere para a porta desejada
```

### Configurar IP Específico
Por padrão o servidor aceita conexões de qualquer IP da rede (`0.0.0.0`). Para restringir, edite:
```python
host = '192.168.1.100'  # IP específico
```

## 📋 Requisitos

- **Python 3.7+**
- **Dependências** (instaladas automaticamente):
  - Flask 2.3.3
  - Flask-SocketIO 5.3.6
  - qrcode[pil] 7.4.2
  - Pillow 10.0.1
  - eventlet 0.33.3

## 🌍 Acesso via Rede

### Descobrir seu IP:
```bash
# Linux/Mac
ip addr show | grep inet
ifconfig | grep inet

# Windows
ipconfig
```

### Exemplo de URLs:
- **IP Local**: `192.168.1.100`
- **Controle**: `http://192.168.1.100:5000/control`
- **Source**: `http://192.168.1.100:5000/source`

## 🔍 Solução de Problemas

### Servidor não inicia
```bash
# Verificar se a porta está livre
netstat -an | grep :5000

# Matar processo na porta
sudo kill -9 $(lsof -t -i:5000)
```

### Não consegue acessar via rede
1. Verifique se está na mesma rede WiFi
2. Desative firewall temporariamente
3. Teste com IP local primeiro
4. Verifique se a porta não está bloqueada

### Lower Thirds não aparecem
1. Verifique console do navegador (F12)
2. Confirme conexão WebSocket
3. Teste painel de controle local primeiro
4. Verifique se OBS está usando URL correta

## 📱 Uso Mobile

1. **Escaneie o QR Code** da página inicial
2. **Ou acesse diretamente**: `http://SEU_IP:5000/control`
3. **Interface otimizada** para touch
4. **Controle completo** dos Lower Thirds

## 🎯 Vantagens sobre Versão Original

- ✅ **Controle remoto** de qualquer dispositivo
- ✅ **Não precisa** estar no mesmo computador
- ✅ **Interface web** moderna e responsiva
- ✅ **QR Code** para acesso rápido
- ✅ **WebSocket** para comunicação instantânea
- ✅ **Compatibilidade total** com arquivos originais

## 🤝 Suporte

Para dúvidas ou problemas:
1. Verifique os logs no terminal
2. Teste acesso local primeiro
3. Confirme configuração de rede
4. Verifique dependências instaladas

## 📄 Licença

Mantém a licença MIT original do projeto Animated Lower Thirds.

---

**🎬 Desenvolvido para facilitar o controle remoto de Lower Thirds via rede!**
