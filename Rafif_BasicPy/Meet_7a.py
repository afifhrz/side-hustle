import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,5000)
y = (4*x**2-2)*np.exp(-(x**2))
print(max(abs(y[1:])))

plt.plot(x,y)
plt.show()