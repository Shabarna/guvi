n1=input().split()
n2=int(n1[2])
n3=n1[0]
n4=n1[1]
s=0
for i in range(0,len(n1[0])):
    if n3[i]!=n4[i]:
        s=s+1
if s==n2:
    print('yes')
else:
    print('no')
