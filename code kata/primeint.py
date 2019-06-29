n1,n2=map(int,input().split())
n=[]
for i in range(n1+1,n2+1):
  if i>1:
    for x in range(2,i):
      if(i%x==0):
        break
    else:
      n.append(x)
print(len(n)+1)
