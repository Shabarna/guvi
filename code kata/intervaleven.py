S,E = map(int, input().split())
start, end = S, E
for num in range(start+1, end): 
    if num % 2 == 0: 
        print(num, end = " ") 
