n1=int(input())
s=0
while(n1!=0):
  a=n1%10
  s=s+(a*a)
  n1=n1//10
print(s)
