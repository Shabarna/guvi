n1,n2=map(int,input().split())
for i in range(1,100001):
  if((i%n1==0) and (i%n2==0)):
    print(i)
break
