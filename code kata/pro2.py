from itertools import combinations
Number,K=input().split()
K=int(K)
length=[]
dd=combinations(Number,len(Number)-K)
for i in list(dd):
  length.append("".join(i))
print(min(l))
