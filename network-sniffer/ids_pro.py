import tkinter as tk
from scapy.all import sniff, IP, TCP
from datetime import datetime
import threading
import matplotlib.pyplot as plt
import requests

# ================= DATA =================
packet_count = 0
ip_counter = {}
port_counter = {}
alerts = []

SUSPICIOUS_PORTS = [4444, 1337, 5555]
COMMON_PORTS = [80, 443, 53]
THRESHOLD = 15

# ================= FUNCTIONS =================

def show_chart():
    if not port_counter:
        print("No data yet")
        return

    # Sort top 5 ports
    sorted_ports = sorted(port_counter.items(), key=lambda x: x[1], reverse=True)[:5]

    ports = [str(p[0]) for p in sorted_ports]
    counts = [p[1] for p in sorted_ports]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(ports, counts)

    plt.xlabel("Top Ports")
    plt.ylabel("Traffic Count")
    plt.title("Top Network Ports by Traffic")

    # Add values on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                 str(height), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


def export_report():
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("=== IDS REPORT ===\n\n")
        f.write(f"Total Packets: {packet_count}\n\n")

        f.write("Top IPs:\n")
        for ip, count in ip_counter.items():
            f.write(f"{ip} -> {count}\n")

        f.write("\nTop Ports:\n")
        for port, count in port_counter.items():
            f.write(f"{port} -> {count}\n")

        f.write("\nAlerts:\n")
        for a in alerts:
            f.write(a + "\n")

    log("📁 Report exported to report.txt")


def check_ip_reputation(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json", timeout=2)
        return res.json().get("org", "Unknown")
    except:
        return "Lookup failed"


def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)


def log_alert(msg):
    alerts.append(msg)
    alert_box.insert(tk.END, msg + "\n")
    alert_box.see(tk.END)


def analyze_packet(packet):
    global packet_count

    if not packet.haslayer(IP) or not packet.haslayer(TCP):
        return

    ip = packet[IP]
    tcp = packet[TCP]

    src_ip = ip.src
    dst_ip = ip.dst
    dst_port = tcp.dport

    packet_count += 1
    packet_label.config(text=f"Packets: {packet_count}")

    # Track stats
    ip_counter[src_ip] = ip_counter.get(src_ip, 0) + 1
    port_counter[dst_port] = port_counter.get(dst_port, 0) + 1

    log(f"{datetime.now().strftime('%H:%M:%S')} | {src_ip} → {dst_ip} | Port {dst_port}")

    # Detection
    if dst_port in SUSPICIOUS_PORTS:
        log_alert(f"[CRITICAL] Suspicious port {dst_port} from {src_ip}")

    if dst_port not in COMMON_PORTS:
        if ip_counter[src_ip] > THRESHOLD:
            log_alert(f"[CRITICAL] Port scanning suspected from {src_ip}")

    if not src_ip.startswith("192.168"):
        org = check_ip_reputation(src_ip)
        log_alert(f"[INFO] External IP {src_ip} ({org})")


def start_sniffing():
    sniff(prn=analyze_packet, store=False, filter="tcp", count=100)

# ================= UI =================

root = tk.Tk()
root.title("🔥 IDS Security Dashboard")
root.geometry("1000x650")
root.configure(bg="#1e1e1e")

header = tk.Label(root, text="Network Intrusion Detection System",
                  font=("Arial", 18, "bold"),
                  bg="#1e1e1e", fg="#00ffcc")
header.pack(pady=10)

packet_label = tk.Label(root, text="Packets: 0",
                        font=("Arial", 12),
                        bg="#1e1e1e", fg="white")
packet_label.pack()

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

log_frame = tk.Frame(frame, bg="#1e1e1e")
log_frame.grid(row=0, column=0, padx=10)

alert_frame = tk.Frame(frame, bg="#1e1e1e")
alert_frame.grid(row=0, column=1, padx=10)

tk.Label(log_frame, text="📡 Traffic Logs",
         bg="#1e1e1e", fg="#00ffcc").pack()

log_box = tk.Text(log_frame, height=20, width=60,
                  bg="#2d2d2d", fg="white")
log_box.pack()

tk.Label(alert_frame, text="🚨 Alerts",
         bg="#1e1e1e", fg="red").pack()

alert_box = tk.Text(alert_frame, height=20, width=40,
                    bg="#2d2d2d", fg="red")
alert_box.pack()

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="📊 Show Chart",
          bg="#333", fg="white",
          command=show_chart).pack(side=tk.LEFT, padx=10)

tk.Button(btn_frame, text="📁 Export Report",
          bg="#333", fg="white",
          command=export_report).pack(side=tk.LEFT, padx=10)

# Start sniffing
threading.Thread(target=start_sniffing, daemon=True).start()

root.mainloop()