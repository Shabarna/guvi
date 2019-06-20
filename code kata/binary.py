a=int(input())
a=str(a)
f=0
for i in range(0,len(a)):
  if(a[i]=='0' or a[i]=='1'):
    f=1
  else:
    f=0
    break
if(f==1):
  print("yes")
else:
  print("no")
