x = 5.0
error = 0.0001
xi = 3.0

while (abs(xi**2-x)>error):
    xi = (xi + x/xi)/2

print(xi)