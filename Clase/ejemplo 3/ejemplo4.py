import numpy as np
def euler(x):
    return 2 * x * (1.0 - x)
t = np.linspace(10.0, 13.0)
h = t[1] - t[0]
xk = np.zeros(t.shape[0])
xk[0] = 0.2
for i in np.arange(xk.shape[0] - 1):
    xk[i + 1] = xk[i] + h * euler(xk[i])


