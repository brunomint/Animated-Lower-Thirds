# 📋 Changelog - Animated Lower Thirds Network Fork

## 🌐 **v2.0.0 - Network Fork** (2025-10-29)

### 🆕 **Novas Funcionalidades**
- ✅ **Servidor Flask integrado** com auto-detecção de IP
- ✅ **Controle remoto via rede WiFi** de qualquer dispositivo
- ✅ **WebSocket em tempo real** para sincronização instantânea
- ✅ **Interface mobile responsiva** otimizada para touch
- ✅ **QR Codes automáticos** para acesso rápido pelo celular
- ✅ **Upload automático de logos** via interface web
- ✅ **Sistema híbrido** (BroadcastChannel + WebSocket)
- ✅ **Multiplataforma** (Windows, Linux, macOS)

### 🔧 **Melhorias Técnicas**
- ✅ **Roteamento Flask** para servir recursos corretamente
- ✅ **API REST** para upload e gerenciamento de logos
- ✅ **Logs detalhados** para debug e monitoramento
- ✅ **Interceptação inteligente** do BroadcastChannel original
- ✅ **Headers anti-cache** para atualizações em tempo real
- ✅ **Tratamento de erros** robusto para recursos não encontrados

### 🎯 **Compatibilidade**
- ✅ **100% compatível** com arquivos originais
- ✅ **Mantém todas as funcionalidades** do projeto base
- ✅ **Não quebra nenhuma feature** existente
- ✅ **Funciona local e em rede** simultaneamente

### 📦 **Arquivos Adicionados**
- `app.py` - Servidor Flask principal com WebSocket
- `start_server.py` - Script de inicialização automática
- `requirements.txt` - Dependências Python
- `templates/index.html` - Página inicial com QR Codes
- `README_FORK.md` - Documentação do fork
- `README_SERVIDOR.md` - Documentação técnica
- `CHANGELOG.md` - Este arquivo

### 🔄 **Arquivos Modificados**
- `control-panel.html` - Integração WebSocket para envio
- `browser-source.html` - Integração WebSocket para recepção
- Correção de paths relativos para absolutos

### 🛠️ **Dependências**
- Flask 2.3.3
- Flask-SocketIO 5.3.6
- QRCode
- Eventlet
- Pillow (para processamento de imagens)

---

## 📜 **v1.6 - Projeto Original** (noeal-dac)

### 🎬 **Funcionalidades Base**
- ✅ Lower Thirds animados para OBS
- ✅ Painel de controle dockável
- ✅ 4 Lower Thirds simultâneos
- ✅ Estilos customizáveis
- ✅ Logos personalizados
- ✅ Comunicação via BroadcastChannel
- ✅ Suporte a hotkeys
- ✅ Fontes customizadas

### 🎯 **Limitações Originais**
- ❌ Apenas Windows (OBS browser panels)
- ❌ Controle local apenas
- ❌ Sem suporte a rede
- ❌ Upload manual de logos

---

## 🤝 **Créditos**

- **Projeto Original**: [noeal-dac/Animated-Lower-Thirds](https://github.com/noeal-dac/Animated-Lower-Thirds)
- **Network Fork**: Implementação de servidor Flask e WebSocket
- **Licença**: MIT (mantida do projeto original)

## 🎯 **Próximas Versões**

### 🔮 **v2.1.0 - Planejado**
- 🔄 Interface de administração web
- 🔄 Múltiplos temas/skins
- 🔄 Backup/restore de configurações
- 🔄 Estatísticas de uso
- 🔄 Suporte a HTTPS

### 🔮 **v2.2.0 - Futuro**
- 🔄 Múltiplas salas/canais
- 🔄 Controle de permissões
- 🔄 Integração com APIs externas
- 🔄 Plugins/extensões
