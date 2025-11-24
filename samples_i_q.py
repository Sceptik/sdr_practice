import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt("My_file.txt")

i_t = data[:, 0]
q_t = data[:, 1]


plt.figure(figsize=(12, 8))

# Амплитудный спектр
plt.subplot(2, 1, 1)
plt.plot(i_t)
plt.title("I(t)")
plt.ylabel("I(t)")
plt.grid(True)

# Фазовый спектр
plt.subplot(2, 1, 2)
plt.plot(q_t)
plt.title("Q(t)")
plt.ylabel("Q(t)")
plt.grid(True)

plt.tight_layout()
plt.show()