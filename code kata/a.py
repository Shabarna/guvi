n1=[]
n2=int(input())
n3=input().split()
for x in n3:
  n1.append(x)
n1.sort()
n1.sort(key=len)
for x in n1:
  print (x,end=' ')
