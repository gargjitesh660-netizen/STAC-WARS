
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 21)

brightness = [
    1.0000, 1.0000, 1.0000, 0.9970, 1.0000,
    1.0000, 1.0000, 1.0000, 0.9970, 1.0000,
    1.0000, 1.0000, 0.9970, 1.0000, 1.0000,
    1.0000, 0.9970, 1.0000, 1.0000, 1.0000,
    0.9970
]

plt.figure(figsize=(10, 5))

plt.plot(time, brightness, marker='o', linestyle='-',
         label='STAC-1')
plt.xlabel("Time (days)")
plt.ylabel("Relative Brightness")
plt.title("STAC-1")


plt.xticks(time)
plt.show()
