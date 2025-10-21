import tkinter as tk
import pandas as pd

# Load received data
df = pd.read_csv("examples/sample_transmission_data.csv")
received_data = df["led_signal"].apply(lambda x: 1 if x > 2 else 0).tolist()

devices = ["Light", "Fan", "AC", "TV"]
device_status = {devices[i]: received_data[i] for i in range(len(devices))}

# Tkinter dashboard
root = tk.Tk()
root.title("Smart Home VLC Dashboard")

for idx, device in enumerate(devices):
    status = "ON" if device_status[device] == 1 else "OFF"
    tk.Label(root, text=f"{device}: {status}", font=("Arial", 16)).pack(pady=5)

root.mainloop()
