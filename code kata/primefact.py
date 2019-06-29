n1=int(input())
for x in range(2,n1+1):
  if(n1%x==0):
      s=0
      for i in range(2,x+1):
          if(x%i==0) and (i!=x):
              s=1
              break
      if(s==0):
print(x,end=' ')
