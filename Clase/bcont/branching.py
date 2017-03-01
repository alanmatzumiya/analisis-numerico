y = 5.0
epsilon = 0.000001
G = 3.0

while not(abs(G**2-y)<epsilon):
    G = (G + y/G)/2

print(G)


