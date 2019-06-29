n1=input()
n2='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
n3=''
for i in n1:
  if i in n2:
    a=n2.index(i)
    a=a+3
    n3=n3+n2[a]
print(n3)
