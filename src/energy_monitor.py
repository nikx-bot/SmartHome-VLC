import matplotlib.pyplot as plt

# Energy assumptions (in Joules)
led_energy_per_bit = 0.5   # energy per bit via VLC
wifi_energy_per_bit = 2.0  # energy per bit via Wi-Fi
num_bits = 20

vlc_energy = led_energy_per_bit * num_bits
wifi_energy = wifi_energy_per_bit * num_bits

print(f"VLC Energy: {vlc_energy} J, Wi-Fi Energy: {wifi_energy} J")

# Plot comparison
plt.bar(["VLC", "Wi-Fi"], [vlc_energy, wifi_energy], color=["yellow", "blue"])
plt.ylabel("Energy Consumption (Joules)")
plt.title("Energy Comparison: VLC vs Wi-Fi")
plt.show()
