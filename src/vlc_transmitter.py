import numpy as np
import pandas as pd

# Simulate data to transmit (ON=1, OFF=0)
data = np.random.randint(0, 2, 20)  # 20-bit random data
print("Data to transmit:", data)

# Simulate LED intensity for VLC
led_signal = data * 5  # LED ON=5 units, OFF=0 units
print("LED Signal:", led_signal)

# Save transmitted signal for receiver
df = pd.DataFrame({"bit": data, "led_signal": led_signal})
df.to_csv("examples/sample_transmission_data.csv", index=False)
print("Transmission saved to sample_transmission_data.csv")
