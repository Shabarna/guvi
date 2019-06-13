S,E = map(int, input().split())
start, end = S, E
for num in range(S+1, E):
      if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=' ')
