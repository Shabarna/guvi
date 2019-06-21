a,b=map(int,input().split())
n=a*b
for i in range(1,n+1):
  if(n==i**2):
    print("yes")
    break
else:
  print("no")
