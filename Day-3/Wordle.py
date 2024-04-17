y=int(input())
k=[]
l=[]
t=''

for i in range(y):
    s=(input())
    T=(input())
    o=len(s)
    for i,j in zip(s,T) :
      if(i==j):
        t=t+'g'
      else:
        t=t+'b'  
    print(t)  
    s=''
    T='' 
    t=''    
    