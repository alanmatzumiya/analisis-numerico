import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, t):
    u = x[0]
    v = x[1]
    f1 = v - 2*u
    f2 = t**2 - v
    return np.array([f1, f2])


x0 = 1
y0 = 0

X0 = [x0, y0]
t = np.linspace(0, 10, 1000)
h = t[1] - t[0]
solode = odeint(f, X0, t)

u = solode[:, 0]
v = solode[:, 1]

u_euler = np.zeros(solode.shape)
u_euler[0] = X0
for i in np.arange(t.shape[0] - 1):
    u_euler[i + 1] = u_euler[i] + h*f(u_euler[i], t[i])


plt.figure()
plt.plot(u, v, label = 'solode')
plt.plot(u_euler[:, 0], u_euler[:, 1], label = 'soleuler')
plt.legend(loc=0)


plt.figure()
plt.plot(t, u)
plt.plot(t, v)

plt.show()

