n1=int(input())
a=[]
for i in range(0,n1):
    b=str(input())
    a.append(b)
def compare(str1,str2):
    n2=len(str1)
    n3=len(str2)
    res=""
    i=0
    j=0
    while(i<=n2-1 and j<=n3-1):
        if(str1[i]==str2[j]):
            res=res+str1[i]
        i=i+1
        j=j+1
    return res
o=[]
for i in range(len(a)-1):
    o.append(compare(a[i],a[i+1]))
    i=i+1
print(*set(o))
