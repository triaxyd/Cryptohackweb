#510143758735509025530880200653196460532653147
#import primefac
from sympy import factorint

def factorize_large_number(number):
    factors = factorint(number)
    return factors

# Example usage:
num = 510143758735509025530880200653196460532653147
result = factorize_large_number(num)

print(f"The prime factors of {num} are: {result}")