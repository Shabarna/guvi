a=input()
b = False
c = False
for i in a:
  if i.isalpha():
      b = True
  if i.isdigit():
      c = True
if b and c:
  print('Yes')
else:
  print('No')
