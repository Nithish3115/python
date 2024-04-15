t=int(input())
f=1

for i in range(t):
  n=int(input())
  for t in range(1,n+1):
     f=f*t
  print(f)
  f=1  