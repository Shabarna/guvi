n1=int(input())
l1=list(map(int,input().split()))
for i in range (len(l1)):
  if(l1[i]>l1[i+1]):
    break
print(i)
