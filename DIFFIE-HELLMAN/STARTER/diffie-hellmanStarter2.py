#https://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number
from sympy import primefactors
p = 28151
phip = p-1
prime_factors = primefactors(phip)
powers_to_test = list(int(phip/pf) for pf in prime_factors)

# test for range 1-100 to see
for i in range(1, 101):
    is_primitive = True
    for pt in powers_to_test:
        if pow(i, pt, p) == 1:
            is_primitive = False
            break 
    if is_primitive:
        print(f'Found smallest primitive root: {i}')
        break 
