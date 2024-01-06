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
'''

ints = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
max_int = max(ints)

