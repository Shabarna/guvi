num=input()
n1=[num[i] for i in range(len(num)) if i%2==0]
n2=[num[i] for i in range(len(num)) if i%2!=0]
for j in range(len(num)//2):
  print(n2[j]+n1[j],end="")
