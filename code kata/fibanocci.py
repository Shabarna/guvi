number=int(input())
a=0
b=1
while(number>0):
  print(b,end=' ')
  a,b=b,a+b
  number=number-1
