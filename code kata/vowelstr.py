a = input()
b = ["a","e","i","o","u","A","E","I","O","U"]
c=len(a)
for i in range(0,c):
  if(a[i] in b):
    print("yes")
    break
else:
  print("no")
