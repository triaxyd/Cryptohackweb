import sympy

#if n is prime => phi(n) = (n-1)
#n = p*q with p,q primes => phi(n) = (p-1) * (q-1)
# n = a*b either a|&b composite => phi(n) = n * (1-1/p1)*(1-1/p2)...

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

N = p*q

def phi(a,b):
    return (a-1) * (b-1)

print(phi(p,q))