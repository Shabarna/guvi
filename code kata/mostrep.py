n1 = input()
n2 = []
for x in range(len(n1)):
  n2.append(n1.count(n1[x]))
x = n2.index(max(n2))
print (n1[x])
