in1,in2=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
	if(a[i]%2!=0):
		b.append(a[i])
print(b[in2-1])
