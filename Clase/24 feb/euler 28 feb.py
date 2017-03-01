import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return(1 - 2 * t) * x

def sol_exacta(t):
    s = np.exp(0.25 - (0.5 - t)**2)
    return s


def euler_method(n_max = 6 , x0 = 1.0):
    t = np.linspace(0, 3, n_max)
    n_size = t.shape[0]
    x = np.zeros(n_size)
    h = t[1] - t[0]


    x[0] = x0

    for j in np.arange(n_size - 1):
        x[j + 1] = x[j] + h * f(x[j], t[j])

    return x
fig_1 = plt.figure()
t_ex = np.linspace(0, 3, 200)
t_euler_1 = np.linspace(0 ,3 ,6)
x_euler_1 = euler_method()
s_exact = sol_exacta(t_ex)

plt.plot(t_euler_1 , x_euler_1, "*")
plt.plot(t_ex, s_exact)
plt.show()


numerical methods for ordinary differential equations
    David griffiths