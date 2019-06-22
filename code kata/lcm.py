import math
s,r=input().split()
s=int(s)
r=int(r)
t=(math.gcd(s,r))
print((s*r)//t)
