number=int(input())
s=0
while(number>0):
  d=number%10
  number=number//10
  s=s+d
print(s)
