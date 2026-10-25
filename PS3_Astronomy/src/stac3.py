import matplotlib.pyplot as plt
import numpy as np

time =np.arange(0,201,10)
brightness=[1.0000,1.0000,0.9990,1.0000,1.0000,1.0000,0.9992,1.0000,1.0000,1.0000,0.9991,1.0000,1.0000,1.0000,0.9993,1.0000,1.0000,0.9990,1.0000,1.0000,1.0000]
plt.plot(time,brightness,marker="o")
plt.title("STAC-3")
plt.xlabel("Time (days)")
plt.ylabel("Relative Brightness")
plt.xticks(time)
plt.show()