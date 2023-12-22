
a1,a2,a3 = 2 , 3 , 5
m1,m2,m3 = 5 , 11 , 17 

M = m1 * m2 * m3
M1,M2,M3 = int(M/m1),int(M/m2),int(M/m3)

iM1,iM2,iM3 = pow(M1, -1, m1), pow(M2,-1,m2) , pow(M3,-1,m3)

x = ((a1*M1*iM1) + (a2*M2*iM2) + (a3*M3*iM3))%M
print(x)

print(pow(209,-1,991))
print(pow(101,17,22663))

