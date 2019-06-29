n1, n2 =[int(i) for i in input().split()]
count =0
for x in range(n2+1):
    k = x*x
    if k in range(n1,n2):
            count+=1
print(count)
