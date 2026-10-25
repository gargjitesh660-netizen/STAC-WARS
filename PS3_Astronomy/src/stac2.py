import numpy as np
import matplotlib.pyplot as plt

time=np.arange(0,201,20)
brightness = [
    1.0000,0.9990,1.0000,1.0000,1.0000,0.9990,1.0000,1.0000,1.0000,0.9990,1.0000
]

plt.plot(time,brightness, marker='o', linestyle='-',
          label='STAC-2')
plt.xlabel("Time (days)")
plt.ylabel("Relative Brightness")
plt.title("STAC-2")

plt.xticks(time)
plt.show()

