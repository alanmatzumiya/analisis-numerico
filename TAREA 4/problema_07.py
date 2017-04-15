import numpy as np
import matplotlib.pyplot as plt

def f(x, t, k):
    return( k*x )

def sol_exacta(t, k, x0):
    s = x0 * np.exp(k*t)
    return s

def TS3(x0, xp, xr, xl, t0, tf, n_size, h, k):
    t3 = np.zeros(n_size)
    TS3 = np.zeros(n_size)

    t3[0] = t0
    TS3[0] = x0
    tn = t0
    i = 1

    while tn <= tf:
        t3[i] = t3[0] + h * i
        tn = t3[i]
        TS3[i] = x0 + h * xp + 0.5 * (h ** 2) * xr + (1.0 / 6.0) * (h ** 3) * xl
        x0 = TS3[i]
        xp = k * x0
        xr = (k **2) * x0
        xl = (k ** 3) * x0
        i = i + 1

    return np.array(t3), np.array(TS3)

k = -10.0
x0 = 1
xp = k * x0
xr = (k**2) * x0
xl = (k**3) * x0
t0 = 0
tf = 10
n_size = 15

t1, x1 = TS3(1 ,-1 ,1 ,-1 ,0 , 10, 102, 0.1, -1)
t2, x2 = TS3(1 ,-1 ,10000 ,-100000 ,0 ,0.5 ,100, 0.01, -100)

fig = plt.figure()
t_ex = np.linspace(0, 10, 200)
s_exact = sol_exacta(t_ex, -1, 1)
plt.plot(t1 , x1, "p", label = 'TS3, lambda = -1')
plt.plot(t_ex, s_exact, label = 'sol_Exact, lambda = -1')
plt.legend(loc=0)

fig = plt.figure()
t_ex = np.linspace(0, 0.5, 200)
s_exact = sol_exacta(t_ex, -100, 1)
plt.plot(t2 , x2, "p", label = 'TS3, lambda = -100')
plt.plot(t_ex, s_exact, label = 'sol_Exact, lambda = -100')
plt.legend(loc=0)

plt.show()
