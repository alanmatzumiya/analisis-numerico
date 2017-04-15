import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    u = x[0]
    v = x[1]
    f1 = v
    f2 = -u
    return np.array([f1, f2])

def TS2(x0, y0, t0, tf, h):

    t0 = 0
    tf = 10
    t = np.linspace(t0, tf, 10000)

    x0 = 1.0
    y0 = 0
    X0 = [x0, y0]

    TS2 = np.zeros([t.shape[0], 2])
    TS2[0] = X0
    for i in np.arange(t.shape[0] - 1):
        TS2[i + 1] = TS2[i] + h*f(TS2[i], t[i]) - (0.5 * h**2) * f(TS2[i], t[i])
    return TS2

t0 = 0
tf = 30
x0 = 1.0
y0 = 0
h = 0.001
t = np.linspace(t0, tf, 10000)

TS2 = TS2(x0, y0, t0, tf, h)

u = TS2[:,0]
v = TS2[:,1]

plt.figure()
plt.plot(u, v, label = 'TS2, U vs V')
plt.legend(loc=0)

plt.figure()
plt.plot(t, u, label = 'TS2, t vs U')
plt.plot(t, v, label = 'TS2, t vs V')
plt.legend(loc=0)

plt.show()