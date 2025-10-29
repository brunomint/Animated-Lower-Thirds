# Animated Lower Thirds - Network Fork 🌐

Este é um fork do excelente projeto [**Animated Lower Thirds**](https://github.com/noeal-dac/Animated-Lower-Thirds) criado por **noeal-dac**, com melhorias significativas para uso em rede e controle remoto.

## 🎯 **Diferenças do Projeto Original**

### **📋 Projeto Original**
- ✅ Lower Thirds animados para OBS
- ✅ Painel de controle dockável
- ✅ Comunicação via BroadcastChannel (local)
- ❌ Limitado ao Windows (OBS browser panels)
- ❌ Controle apenas no mesmo computador
- ❌ Sem suporte a rede

### **🚀 Nossa Versão (Fork)**
- ✅ **Todas as funcionalidades originais mantidas**
- ✅ **Controle remoto via rede WiFi**
- ✅ **Multiplataforma** (Windows, Linux, macOS)
- ✅ **Servidor Flask integrado**
- ✅ **WebSocket para comunicação em tempo real**
- ✅ **Interface mobile responsiva**
- ✅ **QR Codes para acesso rápido**
- ✅ **Upload automático de logos**

## 🆕 **Novas Funcionalidades**

### **🌐 Controle Remoto**
- Controle os Lower Thirds de **qualquer dispositivo** na rede
- **Celular, tablet ou outro computador** como controle remoto
- **Sincronização instantânea** via WebSocket

### **📱 Interface Mobile**
- **QR Codes** para acesso rápido pelo celular
- **Interface responsiva** otimizada para touch
- **Mesma funcionalidade** do painel desktop

### **🖥️ Servidor Flask**
- **Servidor web integrado** com auto-detecção de IP
- **Roteamento adequado** para todos os recursos
- **API REST** para upload de logos
- **Logs detalhados** para debug

### **🔄 Sistema Híbrido**
- **BroadcastChannel** para compatibilidade local
- **WebSocket** para comunicação em rede
- **Funciona simultaneamente** nos dois modos

## 📦 **Arquivos Adicionados**

```
📁 Projeto/
├── 🆕 app.py                 # Servidor Flask principal
├── 🆕 start_server.py        # Script de inicialização
├── 🆕 requirements.txt       # Dependências Python
├── 🆕 README_FORK.md         # Esta documentação
├── 🆕 README_SERVIDOR.md     # Documentação técnica
├── 🆕 templates/
│   └── 🆕 index.html         # Página inicial com QR Codes
├── 🔄 control-panel.html     # Modificado: WebSocket integrado
├── 🔄 browser-source.html    # Modificado: Recepção WebSocket
└── ... (demais arquivos originais mantidos)
```

## 🚀 **Como Usar**

### **1. Instalação**
```bash
# Clone ou baixe este fork
cd Animated-Lower-Thirds

# Instale as dependências (automático)
python3 start_server.py
```

### **2. Acesso**
- **Servidor**: `http://SEU_IP:5000`
- **Controle**: `http://SEU_IP:5000/control`
- **OBS Source**: `http://SEU_IP:5000/source`

### **3. OBS Studio**
1. Adicione uma fonte **"Browser"**
2. URL: `http://SEU_IP:5000/source`
3. Largura: 1920, Altura: 1080

### **4. Controle Mobile**
1. Acesse `http://SEU_IP:5000` no celular
2. Escaneie o QR Code ou clique em "Controle"
3. Configure os Lower Thirds remotamente!

## 🛠️ **Tecnologias Utilizadas**

- **Flask 2.3.3** - Servidor web
- **Flask-SocketIO 5.3.6** - WebSocket em tempo real
- **QRCode** - Geração de QR Codes
- **Eventlet** - Servidor assíncrono
- **HTML5/CSS3/JavaScript** - Interface (original)

## 🎬 **Demonstração**

### **Antes (Original)**
```
PC com OBS → Painel local → Lower Thirds
```

### **Depois (Fork)**
```
Celular → WiFi → Servidor Flask → WebSocket → PC/OBS → Lower Thirds
```

## 🤝 **Créditos e Licença**

### **👨‍💻 Projeto Original**
- **Autor**: [noeal-dac](https://github.com/noeal-dac)
- **Repositório**: [Animated-Lower-Thirds](https://github.com/noeal-dac/Animated-Lower-Thirds)
- **Licença**: MIT

### **🌐 Melhorias de Rede**
- **Implementação**: Fork com servidor Flask e WebSocket
- **Compatibilidade**: 100% com projeto original
- **Licença**: MIT (mantida)

## 💝 **Apoie o Projeto Original**

Se você gostou desta ferramenta, considere apoiar o autor original:
- **PayPal**: [paypal.me/noealdac](https://paypal.me/noealdac)

## 📝 **Licença**

Este fork mantém a licença MIT do projeto original. Veja [LICENSE](LICENSE) para detalhes.

---

**🎯 Resumo**: Este fork adiciona capacidades de rede ao excelente projeto Animated Lower Thirds, permitindo controle remoto via WiFi mantendo 100% de compatibilidade com as funcionalidades originais.
