"""
import numpy as np

p = 29
ints = [14,6,11]

for i in ints:
    quadres = []
    mid = int(np.floor(i/2))
    for n in range(1,mid):
        squaredn = n ** 2
        if squaredn not in quadres : quadres.append(squaredn%p)
    quadres.sort()

    print(f"quadratic residues of {i} = {quadres}")
    """

ints = [14,6,11]
p = 29

for i in ints:
    quadraticres = []
    for a in range(1,29):
        if (a**2) % p == i: quadraticres.append(a)
    print(quadraticres) 

