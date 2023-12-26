#https://math.stackexchange.com/questions/1952453/finding-an-integer-x-and-a-3-digit-prime-p-that-solves-the-problem
'''
import numpy as np
from sympy import primefactors

ints = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

# 3 digit prime p range (100,999) and max in ints is 851
# 588x ≡ 665modp
# 665x ≡ 216modp
# 216x ≡ 113modp
# 113x ≡ 642modp
# 642x ≡ 4modp
#   4x ≡ 836modp
# 836x ≡ 114modp
# 114x ≡ 851modp
# 851x ≡ 492modp
# 492x ≡ 819modp
# 819x ≡ 237modp

for i in ints:
    for j in ints:
        if i==j:break
        for k in range(1,100):
            if (i**k) == (j**k) - 1: print(i,j,k,l,"\n")
            for l in range(1,100):
                if (i**k) == (j**l)-1: print(i,j,k,l,"\n")
                if (i**k) == (j**l)+1: print(i,j,k,l,"\n")
                if (j**k) == (i**l)-1: print(i,j,k,l,"\n")
                if (j**k) == (i**l)+1: print(i,j,k,l,"\n")

# 114x ≡ 851modp
# 113x ≡ 642modp
# subtract and we have x ≡ 209modp
# 113 * 209 ≡ 642 -> p | 642+133*209
print(primefactors(642+(133*209)))
'''

from sympy.ntheory.modular import solve_congruence

residues = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
for p in range (max(residues),999):
    result = solve_congruence(residues, [p**i for i in range(11, 0, -1)])
    p, x = result[0], result[1]
    print(f"The prime p is: {p}")
    print(f"The integer x is: {x}")

