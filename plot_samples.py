import numpy as np
import matplotlib.pyplot as plt

name = "txdata.pcm"

data = []
imag = []
real = []
count = []
counter = 0
with open(name, "rb") as f:
    index = 0
    while (byte := f.read(2)):
        if(index %2 == 0):
            real.append(int.from_bytes(byte, byteorder='little', signed=True))
            counter += 1
            count.append(counter)
        else:
            imag.append(int.from_bytes(byte, byteorder='little', signed=True))
        index += 1

real = np.asarray(real)
imag = np.asarray(imag)
complex = real + imag * 1j
plt.figure(1)
plt.stem(abs(complex))  # Используем scatter для диаграммы созвездия
  # Используем scatter для диаграммы созвездия
plt.show()