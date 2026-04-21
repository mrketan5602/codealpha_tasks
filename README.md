# 🔥 Network Intrusion Detection System (IDS)

A Python-based **real-time Intrusion Detection System (IDS)** that monitors network traffic, detects suspicious activities, and provides alerts with visualization and reporting.

---

## 🚀 Features

- 📡 Real-time packet capture using Scapy  
- 🚨 Alert system (INFO / WARNING / CRITICAL)  
- 🔍 Suspicious port detection (e.g. 4444, 1337)  
- 🧠 Basic port scanning / flooding detection  
- 🌐 External IP tracking with organization lookup  
- 📊 Traffic visualization (Top Ports Chart)  
- 📁 Report generation (`report.txt`)  
- 🖥️ GUI Dashboard (Tkinter-based)

---

## 🛠️ Tech Stack

- Python  
- Scapy (packet capture & analysis)  
- Tkinter (GUI dashboard)  
- Matplotlib (data visualization)  
- Requests (IP reputation lookup)

---

## 📊 How It Works

1. Captures live TCP packets from the network  
2. Extracts key data:
   - Source IP  
   - Destination IP  
   - Port numbers  
3. Applies detection rules:
   - Suspicious ports  
   - Unusual traffic behavior  
   - High request rate (possible scanning)  
4. Generates alerts based on severity  
5. Displays results in a real-time dashboard  
6. Allows exporting logs as a report  

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install scapy matplotlib requests

2. Run the program
python ids_pro.py
⚠️ Important
Run as Administrator (required for packet sniffing)
Generate traffic (browser / ping) to see activity
📊 Features in Action
📡 Live traffic logs updating in real-time
🚨 Alerts displayed separately for quick analysis
📊 Chart showing most active ports
📁 Exportable report for analysis
📁 Output Files
alerts.log → Stores alert logs
report.txt → Generated report with:
Total packets
Top IPs
Top ports
Alerts
🎯 Use Case

This project demonstrates core SOC / Blue Team concepts:

Network traffic analysis
Intrusion detection basics
Behavior-based monitoring
Alerting systems
⚠️ Limitations
Basic rule-based detection (not AI/ML)
Works on TCP traffic only
Limited to local machine/network visibility
🔮 Future Improvements
Advanced anomaly detection
Real-time graphs (live monitoring)
Integration with threat intelligence APIs
Better UI (PyQt / Web dashboard)
⚠️ Disclaimer

This project is for educational purposes only.
Do not use it for unauthorized network monitoring.

👨‍💻 Author

Ketan Jadhav
BCA Student | Aspiring SOC Analyst

⭐ If you found this useful

Give it a ⭐ and share your feedback!


---

# 💣 Brutal truth

This README:
👉 makes your project look serious  
👉 explains value clearly  
👉 shows you understand SOC concepts  

---

# 🚀 What you do NEXT (don’t skip)

1. Create `README.md`  
2. Paste this  
3. Push to GitHub  
4. Add screenshot of dashboard  

---

# 🎯 If you want FINAL edge

Say:
👉 **“linkedin post + github description”**

That’s what actually gets you noticed.