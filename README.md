# Animated Lower Thirds - Network Fork 🌐

This is a fork of the excellent [**Animated Lower Thirds**](https://github.com/noeal-dac/Animated-Lower-Thirds) project created by **noeal-dac**, with significant improvements for network usage and remote control.

## 🎯 **Differences from Original Project**

### **📋 Original Project**
- ✅ Animated Lower Thirds for OBS
- ✅ Dockable control panel
- ✅ BroadcastChannel communication (local)
- ❌ Limited to Windows (OBS browser panels)
- ❌ Control only on same computer
- ❌ No network support

### **🚀 Our Version (Fork)**
- ✅ **All original features maintained**
- ✅ **Remote control via WiFi network**
- ✅ **Cross-platform** (Windows, Linux, macOS)
- ✅ **Integrated Flask server**
- ✅ **WebSocket for real-time communication**
- ✅ **Responsive mobile interface**
- ✅ **QR Codes for quick access**
- ✅ **Automatic logo upload**

## 🆕 **New Features**

### **🌐 Remote Control**
- Control Lower Thirds from **any device** on the network
- **Phone, tablet or another computer** as remote control
- **Instant synchronization** via WebSocket

### **📱 Mobile Interface**
- **QR Codes** for quick access from phone
- **Responsive interface** optimized for touch
- **Same functionality** as desktop panel

### **🖥️ Flask Server**
- **Integrated web server** with auto IP detection
- **Proper routing** for all resources
- **REST API** for logo upload
- **Detailed logs** for debugging

### **🔄 Hybrid System**
- **BroadcastChannel** for local compatibility
- **WebSocket** for network communication
- **Works simultaneously** in both modes

## 📦 **Added Files**

```
📁 Project/
├── 🆕 app.py                 # Main Flask server
├── 🆕 start_server.py        # Initialization script
├── 🆕 requirements.txt       # Python dependencies
├── 🆕 README_FORK.md         # This documentation
├── 🆕 README_SERVIDOR.md     # Technical documentation
├── 🆕 templates/
│   └── 🆕 index.html         # Home page with QR Codes
├── 🔄 control-panel.html     # Modified: WebSocket integrated
├── 🔄 browser-source.html    # Modified: WebSocket reception
└── ... (other original files maintained)
```

## 🚀 **How to Use**

### **1. Installation**
```bash
# Clone or download this fork
cd Animated-Lower-Thirds

# Install dependencies (automatic)
python3 start_server.py
```

### **2. Access**
- **Server**: `http://YOUR_IP:5000`
- **Control**: `http://YOUR_IP:5000/control`
- **OBS Source**: `http://YOUR_IP:5000/source`

### **3. OBS Studio**
1. Add a **"Browser"** source
2. URL: `http://YOUR_IP:5000/source`
3. Width: 1920, Height: 1080

### **4. Mobile Control**
1. Access `http://YOUR_IP:5000` on your phone
2. Scan the QR Code or click "Control"
3. Configure Lower Thirds remotely!

## 🛠️ **Technologies Used**

- **Flask 2.3.3** - Web server
- **Flask-SocketIO 5.3.6** - Real-time WebSocket
- **QRCode** - QR Code generation
- **Eventlet** - Asynchronous server
- **HTML5/CSS3/JavaScript** - Interface (original)

## 🎬 **Demonstration**

### **Before (Original)**
```
PC with OBS → Local panel → Lower Thirds
```

### **After (Fork)**
```
Phone → WiFi → Flask Server → WebSocket → PC/OBS → Lower Thirds
```

## 🤝 **Credits and License**

### **👨‍💻 Original Project**
- **Author**: [noeal-dac](https://github.com/noeal-dac)
- **Repository**: [Animated-Lower-Thirds](https://github.com/noeal-dac/Animated-Lower-Thirds)
- **License**: MIT

### **🌐 Network Improvements**
- **Implementation**: Fork with Flask server and WebSocket
- **Compatibility**: 100% with original project
- **License**: MIT (maintained)

## 💝 **Support the Original Project**

If you liked this tool, consider supporting the original author:
- **PayPal**: [paypal.me/noealdac](https://paypal.me/noealdac)

## 📝 **License**

This fork maintains the MIT license from the original project. See [LICENSE](LICENSE) for details.

---

**🎯 Summary**: This fork adds network capabilities to the excellent Animated Lower Thirds project, enabling remote control via WiFi while maintaining 100% compatibility with original features.
