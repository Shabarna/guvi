s,e = map(int, input().split())
start, end = s, e
for num in range(start+1, end): 
    if num % 2 != 0: 
        print(num, end = " ") 
