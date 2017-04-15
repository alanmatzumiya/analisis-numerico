import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return ((1 - 2 * t) * x)


def sol_exact(t):
    s = (np.exp(0.25 - (t - 0.5) ** 2))
    return s


def TS1(x0, xp, t0, tf, n_size, h):

        t1 = np.zeros(n_size)
        TS1 = np.zeros(n_size)

        t1[0] = t0
        TS1[0] = x0
        tn = t0
        i = 1

        while tn <= tf:
            t1[i] = t1[0] + h * i
            tn = t1[i]
            TS1[i] = x0 + h * xp
            x0 = TS1[i]
            xp = (1.0 - 2.0 * t1[i]) * x0
            i = i + 1

        return np.array(t1), np.array(TS1)


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
        xp = (1.0 - 2.0 * t2[i]) * x0
        xr = ((1.0 - 2.0 * t2[i]) ** 2 - 2.0) * x0
        i = i + 1

    return np.array(t2), np.array(TS2)

x0 = 1
xp = 1
xr = -1
t0 = 0
tf = 4



t1, x1 = TS2(1 ,1 ,-1 , 0, 4, 30, 0.15)
t2, x2 = TS2(1 ,1 ,-1 , 0, 4, 30, 0.30)
t3, x3 = TS1(1 , 1, 0, 4, 30, 0.15)
t4, x4 = TS1(1 , 1, 0, 4, 30, 0.30)

print "h".center(12), "TS(1)".center(2), "TS(2)".center(12), "GE, TS(1)".center(0), "GE con el nuevo metodo"
SE = sol_exact(1.2)
GE1 = SE - x4[4]
GE3 = SE - x3[8]

print '{0: 4f} {1: 4f} {2: 4f} {3: 10f} {4: 15f}'.format(0.3, x4[4] , x2[4], GE1, x2[4] - x4[4])
print '{0: 4f} {1: 4f} {2: 4f} {3: 10f} {4: 15f}'.format(0.15, x3[8] , x1[8], GE3, x1[8] - x3[8])