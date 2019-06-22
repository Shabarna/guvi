in1=input()
r=""
for a in in1:
  if a not in r:
    r=r+a
if(in1==r):
  print("Yes")
else:
  print("No")
