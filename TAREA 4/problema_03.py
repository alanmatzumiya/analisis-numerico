import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return( 2 * x * ( 1 - x ) )

def sol_exacta(t):
    s = 1 / (1 + 4 * (np.exp(2 * (10 - t))))
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
        xp = f(x0, t1[i])
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
        xp = f(x0, t2[i])
        xr = 2*xp * (1 - 2*x0)
        i = i + 1

    return np.array(t2), np.array(TS2)

xr = 0.384
x0 = 0.2
t0 = 10
tf = 13
n_size = 15

t1, x1 = TS1(0.2 ,0.32 ,10 , 13, 17, 0.2)
t2, x2 = TS2(0.2 ,0.32 ,0.384 ,10 ,13 ,8, 0.5)

print "t".center(6), "euler method".center(17), "TS2".center(13), "GE Euler".center(17), "GE TS2".center(15)
s = sol_exacta(11.0)
print '{0: 4d} {1: 15f} {2: 15f} {3: 15f} {4: 20}'.format(11, x1[5] , x2[2], abs(x1[5] - s), abs(x2[2] - s))


fig = plt.figure()
t_ex = np.linspace(10, 13, 200)
s_exact = sol_exacta(t_ex)
plt.plot(t1 , x1, "p")
plt.plot(t2 , x2, "o")
plt.plot(t_ex, s_exact)

plt.show()

