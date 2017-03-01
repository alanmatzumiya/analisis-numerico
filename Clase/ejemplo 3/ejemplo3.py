import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(10.0, 13.0)
x = 1.0 / (1 + 4 * np.exp(2 * (10 - t)))
plt.plot(t, x)
plt.show()
