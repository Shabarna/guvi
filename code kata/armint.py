S,E = map(int,input().split())
for n in range(S+1,E):
  sum = 0
  temp = n
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp//10
  if n == sum:
    print(n,end=' ')
