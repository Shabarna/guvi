N,K=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in a:
  if(i==K):
    count=count+1
print(count)
