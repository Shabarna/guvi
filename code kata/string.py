num=input()
a=0
for i in range(len(num)):
  if(num[i].isdigit() or num[i].isalpha() or num[i]==' '):
    continue
  else:
    a=a+1  
print(a)
