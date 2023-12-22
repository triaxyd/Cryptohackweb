
import numpy as np

v = (2,6,3)
w = (1,0,0)
u = (7,7,2)

vv = np.array(v)
vw = np.array(w)
vu = np.array(u)

# 3*(2*v - w) ∙ 2*u
temp1 = 3*((2*vv) - vw)
temp2 = 2*vu
result = np.dot(temp1,temp2)
print(result)



