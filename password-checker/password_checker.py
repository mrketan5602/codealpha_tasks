import tkinter as tk
import math
import re

common_patterns = ["123", "abc", "password", "qwerty", "admin"]

def calculate_entropy(password):
    charset = 0
    if re.search("[a-z]", password):
        charset += 26
    if re.search("[A-Z]", password):
        charset += 26
    if re.search("[0-9]", password):
        charset += 10
    if re.search("[@#$%^&*!]", password):
        charset += 10

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


def analyze_password():
    password = entry.get()
    entropy = calculate_entropy(password)
    feedback = []

    # Pattern detection
    for pattern in common_patterns:
        if pattern in password.lower():
            feedback.append(f"⚠ Contains pattern: {pattern}")

    # Strength logic
    if entropy < 40:
        strength = "Weak"
        color = "#ef4444"
        percent = 30
    elif entropy < 70:
        strength = "Medium"
        color = "#f59e0b"
        percent = 60
    else:
        strength = "Strong"
        color = "#22c55e"
        percent = 100

    # Crack time estimate
    guesses_per_sec = 1e9
    crack_time = (2 ** entropy) / guesses_per_sec

    if crack_time < 60:
        time_str = "Instant"
    elif crack_time < 3600:
        time_str = "Minutes"
    elif crack_time < 86400:
        time_str = "Hours"
    elif crack_time < 31536000:
        time_str = "Days"
    else:
        time_str = "Years+"

    # Update bar
    canvas.coords(bar, 0, 0, percent * 3, 20)
    canvas.itemconfig(bar, fill=color)

    # Output text
    result = f"Strength: {strength}\nEntropy: {entropy:.2f} bits\nCrack Time: {time_str}"

    if feedback:
        result += "\n\n" + "\n".join(feedback)

    output.config(text=result, fg=color)


# UI Setup
root = tk.Tk()
root.title("🔐 Password Security Analyzer")
root.geometry("500x400")
root.configure(bg="#0f172a")

# Title
tk.Label(root, text="Password Security Analyzer",
         bg="#0f172a", fg="white",
         font=("Segoe UI", 16, "bold")).pack(pady=15)

# Input box
entry = tk.Entry(root, width=30, show="*", font=("Segoe UI", 12))
entry.pack(pady=10)

# Button
tk.Button(root, text="Analyze",
          command=analyze_password,
          bg="#3b82f6", fg="white",
          font=("Segoe UI", 10, "bold"),
          relief="flat", padx=10, pady=5).pack(pady=10)

# Strength bar
canvas = tk.Canvas(root, width=300, height=20,
                   bg="#1e293b", highlightthickness=0)
canvas.pack(pady=10)
bar = canvas.create_rectangle(0, 0, 0, 20, fill="#22c55e")

# Output
output = tk.Label(root, text="",
                  bg="#0f172a", fg="white",
                  font=("Segoe UI", 11),
                  justify="left")
output.pack(pady=15)

root.mainloop()