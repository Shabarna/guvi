n1=int(input())
n2=[int(x) for x in input().split()]
n3=0
for x in range(n1):
   for y in range(x):
      if n2[y]<n2[x]:
         n3+=n2[y]
print(n3) 
