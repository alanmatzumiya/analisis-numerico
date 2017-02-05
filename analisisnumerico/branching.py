import numpy as np
n = 11
if n % 2 == 0:
    cont = n/2
else:
    cont = (n + 1) / 2
A = [1]
for cand in np.arange(2 , cont + 1):
    if n % cand == 0:
        A.append(cand)
if n > 1:
    A.append(n)
print A







