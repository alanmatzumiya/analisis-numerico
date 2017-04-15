import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return( 1 + t - x)

def TS2(x0, xp, xr, t0, tf, n_size, h):
    t2 = np.zeros(n_size)
    TS2 = np.zeros(n_size)

    t2[0] = t0
    TS2[0] = x0
    tn = t0
    i = 1

    while tn <= tf:
        t2[i] = t2[0] + h * i
        tn = t2[i]
        TS2[i] = x0 + h * xp + 0.5 * (h ** 2) * xr
        x0 = TS2[i]
        xp = f(x0, t2[i])
        xr = 1 - xp
        i = i + 1

    return np.array(t2), np.array(TS2)

xr = 0
xp = 1
x0 = 0
t0 = 0
tf = 10
n_size = 30

t1, x1 = TS2(0 ,1.0 ,0 ,0 ,10 ,22 ,0.5)

print "t".center(10), "xn".center(7)

for i in np.arange(1, 22):
    print '{0: 2f} {1: 2f}'.format(t1[i], x1[i])

fig = plt.figure()
plt.plot(t1 , x1, "p")

plt.show()
