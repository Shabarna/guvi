n1=int(input())
n2=input()
t=0
n3=['a','e','i','o','u']
for k in n3:
  if(k in n3):
    n2=n2.replace(k,'')
print(n2[::-1])
