import numpy as np
import matplotlib.pyplot as plt

def f(x, t, k):
    return( k*x )

def sol_exacta(t, k, x0):
    s = x0 * np.exp(k*t)
    return s

def TS2(x0, xp, xr, t0, tf, n_size, h, k):
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
        xp = k * x0
        xr = (k **2) * x0
        i = i + 1

    return np.array(t2), np.array(TS2)

k = -10.0
x0 = 1
xp = k * x0
xr = (k**2) * x0
t0 = 0
tf = 10
n_size = 15

t1, x1 = TS2(1 ,-1 ,1 ,0, 10, 102, 0.1, -1)
t2, x2 = TS2(1 ,-100 ,10000 ,0 ,0.5 ,100, 0.01, -100)

fig = plt.figure()
t_ex = np.linspace(0, 10, 200)
s_exact = sol_exacta(t_ex, -1, 1)
plt.plot(t1 , x1, "p", label = 'TS2, lambda = -1')
plt.plot(t_ex, s_exact, label = 'sol_Exact, lambda = -1')
plt.legend(loc=0)

fig = plt.figure()
t_ex = np.linspace(0, 0.5, 200)
s_exact = sol_exacta(t_ex, -100, 1)
plt.plot(t2 , x2, "p", label = 'TS2, lambda = -100')
plt.plot(t_ex, s_exact, label = 'sol_Exact, lambda = -100')
plt.legend(loc=0)

plt.show()
