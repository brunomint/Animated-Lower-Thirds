# 🎬 Animated Lower Thirds - Flask Server

This project is a fork of the original [Animated Lower Thirds](https://github.com/noeal-dac/Animated-Lower-Thirds) created by **noeal-dac**, with the addition of a Flask server for remote control via network from any device.

> **📋 See also**: [README_FORK_EN.md](README_FORK_EN.md) for complete comparison with the original project.

## 🚀 Quick Start

### Option 1: Automatic Initialization (Recommended)
```bash
python start_server.py
```

### Option 2: Manual Initialization
```bash
# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

## 📱 How to Use

### 1. **Local Access**
- Open your browser at: `http://localhost:5000`
- You'll see a page with QR Codes and direct links

### 2. **Remote Control**
- **Control Panel**: `http://YOUR_IP:5000/control`
- **Browser Source (OBS)**: `http://YOUR_IP:5000/source`
- **QR Code**: Scan with your phone for quick access

### 3. **OBS Configuration**
1. Add a **"Browser"** source
2. Use URL: `http://YOUR_IP:5000/source`
3. Set resolution: 1920x1080
4. Configure FPS: 30

## 🌐 Features

### ✅ **Network Control**
- Control from any device on the same WiFi
- Real-time synchronization via WebSocket
- Responsive interface for mobile and desktop

### ✅ **Full Compatibility**
- Maintains all original files
- Works with existing configurations
- Support for hotkeys and shortcuts

### ✅ **Advanced Features**
- QR Code for quick access
- Automatic local IP detection
- Modern and intuitive interface
- Real-time bidirectional communication

## 🔧 Advanced Configuration

### Change Port
Edit the `app.py` file at line:
```python
port = 5000  # Change to desired port
```

### Configure Specific IP
By default the server accepts connections from any network IP (`0.0.0.0`). To restrict, edit:
```python
host = '192.168.1.100'  # Specific IP
```

## 📋 Requirements

- **Python 3.7+**
- **Dependencies** (installed automatically):
  - Flask 2.3.3
  - Flask-SocketIO 5.3.6
  - qrcode[pil] 7.4.2
  - Pillow 10.0.1
  - eventlet 0.33.3

## 🌍 Network Access

### Find your IP:
```bash
# Linux/Mac
ip addr show | grep inet
ifconfig | grep inet

# Windows
ipconfig
```

### Example URLs:
- **Local IP**: `192.168.1.100`
- **Control**: `http://192.168.1.100:5000/control`
- **Source**: `http://192.168.1.100:5000/source`

## 🔍 Troubleshooting

### Server won't start
```bash
# Check if port is free
netstat -an | grep :5000

# Kill process on port
sudo kill -9 $(lsof -t -i:5000)
```

### Can't access via network
1. Check if you're on the same WiFi network
2. Temporarily disable firewall
3. Test with local IP first
4. Check if port is not blocked

### Lower Thirds don't appear
1. Check browser console (F12)
2. Confirm WebSocket connection
3. Test local control panel first
4. Check if OBS is using correct URL

## 📱 Mobile Usage

1. **Scan the QR Code** from the home page
2. **Or access directly**: `http://YOUR_IP:5000/control`
3. **Touch-optimized interface**
4. **Complete control** of Lower Thirds

## 🎯 Advantages over Original Version

- ✅ **Remote control** from any device
- ✅ **No need** to be on the same computer
- ✅ **Modern and responsive** web interface
- ✅ **QR Code** for quick access
- ✅ **WebSocket** for instant communication
- ✅ **Full compatibility** with original files

## 🤝 Support

For questions or problems:
1. Check logs in terminal
2. Test local access first
3. Confirm network configuration
4. Check installed dependencies

## 📄 License

Maintains the original MIT license from the Animated Lower Thirds project.

---

**🎬 Developed to facilitate remote control of Lower Thirds via network!**
