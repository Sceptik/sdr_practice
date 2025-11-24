import numpy as np
import matplotlib.pyplot as plt

name = "txdata1.pcm"

real = []
imag = []
count = []
counter = 0
L = 10

with open(name, "rb") as f:
    index = 0
    while (bytes_data := f.read(2 * L)):
        if index % 2 == 0:
            # Чтение I-компоненты (четные индексы)
            for i in range(0, len(bytes_data), 2):
                if i + 2 <= len(bytes_data):
                    value = int.from_bytes(bytes_data[i:i+2], byteorder='little', signed=True)
                    real.append(value)
                    counter += 1
                    count.append(counter)
        else:
            # Чтение Q-компоненты (нечетные индексы)
            for i in range(0, len(bytes_data), 2):
                if i + 2 <= len(bytes_data):
                    value = int.from_bytes(bytes_data[i:i+2], byteorder='little', signed=True)
                    imag.append(value)
        index += 1

# Проверка данных
print(f"Всего I samples: {len(real)}")
print(f"Всего Q samples: {len(imag)}")
print(f"Уникальные значения I: {set(real)}")
print(f"Уникальные значения Q: {set(imag)}")

# Проверяем, что массивов одинаковой длины
min_len = min(len(real), len(imag))
real = real[:min_len]
imag = imag[:min_len]
count = count[:min_len]

print(f"После выравнивания: I={len(real)}, Q={len(imag)}")

# Создаем графики
plt.figure(figsize=(12, 8))

# Constellation diagram
plt.subplot(2, 1, 1)
plt.scatter(real, imag, color='red', alpha=0.6, s=20)
plt.xlabel("I")
plt.ylabel("Q")
plt.title("Signal constellation")
plt.grid(True, alpha=0.3)

# Time domain signals
plt.subplot(2, 1, 2)
plt.plot(count, real, color='blue', label='I', linewidth=1)
plt.plot(count, imag, color='red', label='Q', linewidth=1)
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.title("Signal in time domain")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Дополнительная диагностика
print(f"\nДиапазон I: [{min(real)}, {max(real)}]")
print(f"Диапазон Q: [{min(imag)}, {max(imag)}]")