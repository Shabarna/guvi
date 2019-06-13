x = int(input())
if(x==1):
  print(t)
elif(x==2):
  s,h=map(int,input().split())
  if(s<h):
    print(s)
  else:
    print(h)
elif(x==3):
  s,h,a=map(int,input().split())
  if((s<h) and (s<a)):
    print(s)
  elif((h<s) and (h<a)):
    print(h)
  else:
    print(a)
elif(x==4):
  s,h,a,b=map(int,input().split())
  if((s<h) and (s<a) and (s<b)):
    print(s)
  elif((h<s) and (h<a) and (h<b)):
    print(h)
  elif((a<h) and (a<s) and (a<b)):
    print(a)
  elif((b<h) and (b<a) and (b<s)):
    print(b)
elif(x==5):
  s,h,a,b,A=map(int,input().split())
  if((s<h) and (s<a) and (s<b) and (s<A)):
    print(s)
  elif((h<s) and (h<a) and (h<b) and (h<A)):
    print(h)
  elif((a<h) and (a<s) and (a<b) and (a<A)):
    print(a)
  elif((b<h) and (b<a) and (b<s) and (b<A)):
    print(b)
  else:
    print(A)
else:
  s,h,a,b,A,r=map(int,input().split())
  if((s<h) and (s<a) and (s<b) and (s<A) and (s<r)):
    print(s)
  elif((h<s) and (h<a) and (h<b) and (h<A) and (h<r)):
    print(h)
  elif((a<h) and (a<s) and (a<b) and (a<A) and (a<r)):
    print(a)
  elif((b<h) and (b<a) and (b<s) and (b<A) and (b<r)):
    print(b)
  elif((A<s) and (A<h) and (A<a) and (A<b) and (A<r)):
    print(A)
  else:
    print(r)
