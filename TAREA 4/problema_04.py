import numpy as np
import matplotlib.pyplot as plt
import math

def f(x, t):
    u = x[0]
    v = x[1]
    f1 = v
    f2 = -u
    return np.array([f1, f2])
def g(x, t):
    u = x[0]
    v = x[1]
    f1 = -u
    f2 = v
    return np.array([f1, f2])

def TS1(x0, y0, t0, tf, h):

    t0 = 0
    tf = 10
    t = np.linspace(t0, tf, 101)

    x0 = math.pi/10.0
    y0 = 0
    X0 = [x0, y0]



    TS1 = np.zeros([t.shape[0], 2])
    TS1[0] = X0
    for i in np.arange(t.shape[0] - 1):
        TS1[i + 1] = TS1[i] + h*f(TS1[i], t[i])
    return TS1

def TS2(x0, y0, t0, tf, h):

    t0 = 0
    tf = 10
    t = np.linspace(t0, tf, 101)

    x0 = math.pi/10.0
    y0 = 0
    X0 = [x0, y0]


    TS2 = np.zeros([t.shape[0], 2])
    TS2[0] = X0
    for i in np.arange(t.shape[0] - 1):
        TS2[i + 1] = TS2[i] + h*f(TS2[i], t[i]) + (0.5 * h**2) * g(TS2[i], t[i])
    return TS2

t0 = 0
tf = 10
x0 = math.pi/10.0
y0 = 0
h = 0.1
t = np.linspace(t0, tf, 101)

TS1 = TS1(x0, y0, t0, tf, h)
TS2 = TS2(x0, y0, t0, tf, h)

w = TS1[:,0]
k = TS1[:,1]
u = TS2[:,0]
v = TS2[:,1]

print "t".center(14), "TS(1)".center(3), "TS(2)".center(11)
print 'U' , '{0: 4f} {1: 4f} {2: 4f}'.format(t[2], w[2] ,u[2])
print 'V', '{0: 4f} {1: 4f} {2: 4f}'.format(t[2], k[2] ,v[2])

plt.figure()
plt.plot(w, k, label = 'TS1, V vs U')
plt.legend(loc=0)

plt.figure()
plt.plot(t, w, label = 'TS1, t vs U')
plt.plot(t, k, label = 'TS1, t vs V')
plt.legend(loc=0)

plt.figure()
plt.plot(u, v, label = 'TS2, U vs V')
plt.legend(loc=0)

plt.figure()
plt.plot(t, u, label = 'TS2, t vs U')
plt.plot(t, v, label = 'TS2, t vs V')
plt.legend(loc=0)

plt.show()

