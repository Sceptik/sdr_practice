import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt("My_file.txt")
samples = np.zeros(len(data), dtype=complex)

for i in range(len(data)):
    samples[i] = complex(data[i][0], data[i][1])

fft_result = np.fft.fft(samples)

amplitude = abs(samples)
phi = np.angle(samples)

plt.figure(figsize=(12, 8))

# Амплитудный спектр
plt.subplot(2, 1, 1)
plt.plot(amplitude)
plt.title("Амплитудный спектр")
plt.ylabel("Амплитуда")
plt.grid(True)

# Фазовый спектр
plt.subplot(2, 1, 2)
plt.plot(phi)
plt.title("Фазовый спектр")
plt.ylabel("Фаза в радианах")
plt.grid(True)

plt.tight_layout()
plt.show()