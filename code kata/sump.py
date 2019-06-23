in1,in2,in3=map(int,input().split())
s=0
for i in range(1,in3+1):
 s+=in1+(in3-i)*in2
print(s)
