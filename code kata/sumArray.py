N=input()
N=N.split()
a=int(N[0])
b=int(N[1])
K=input()
K=K.split()
x=0
r=[]
s=[]
for i in N:
    r.append(int(i))
for j in K:
    s.append(j)
if(b<=a):
    for i in range(0,b):
        x=x+int(s[i])
print(x)
