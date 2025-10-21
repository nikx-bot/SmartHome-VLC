import pandas as pd

# Load transmitted signal
df = pd.read_csv("examples/sample_transmission_data.csv")
led_signal = df["led_signal"].values

# Decode: >2 units = 1, <=2 units = 0
received_data = [1 if val > 2 else 0 for val in led_signal]

print("Received Data:", received_data)
