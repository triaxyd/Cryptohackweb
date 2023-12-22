import RSAstarter3
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
# private key d is the modular multiplicative inverse of exponent e modulo the totient of N

N = RSAstarter3.phi(p,q)
d = pow(e,-1,N)
print(d)