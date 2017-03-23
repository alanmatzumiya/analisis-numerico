import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x, t):
    u = x[0]
    v = x[1]
    f1 = v
    f2 = t**2 - 3*v - 2*u
    return np.array([f1, f2])

def g(x, t):
    s = x[0]
    p = x[1]
    g1 = p - 2*s
    g2 = t**2 - p
    return np.array([g1, g2])

print "t".center(10), "x".center(20), "y".center(0)
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
print 'Para t2 el sistema del inciso a)'
print t[2], u_euler[2]

x0 = 1
y0 = -0.04

X0 = [x0, y0]
t = np.linspace(0, 10, 1000)
h = t[1] - t[0]
solode = odeint(g, X0, t)

s = solode[:, 0]
p = solode[:, 1]

u_euler1 = np.zeros(solode.shape)
u_euler1[0] = X0
for i in np.arange(t.shape[0] - 1):
    u_euler1[i + 1] = u_euler1[i] + h*g(u_euler1[i], t[i])
print 'Para t2 el sistema del inciso b)'
print t[2], u_euler1[2]

plt.figure()
plt.plot(u, v, label = 'solode')
plt.plot(u_euler[:, 0], u_euler[:, 1], label = 'soleuler')
plt.legend(loc=0)


plt.figure()
plt.plot(t, u)
plt.plot(t, v)

plt.show()


