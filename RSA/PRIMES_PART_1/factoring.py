from sympy import factorint

def factorize(number):
    factors = factorint(number)
    return factors

num = 510143758735509025530880200653196460532653147
result = factorize(num)

print(f"The prime factors of {num} are: {result}")