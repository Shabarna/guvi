a=int(input())
if (a>1):
  for b in range(2,a):
    if (a % b==0):
      print('no')
      break
  else:
    print('yes')  
else:
  print('no') 
