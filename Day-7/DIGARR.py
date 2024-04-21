 # cook your dish here
t=int(input())
k=['0','5']
p=0
for i in range(t):
    d=int(input())
    n=int(input())
    n=str(n)
    for j in n:
        if j in k:
            p=p+1
 
        else:
            p=p+0
    if(p>=1):
       print("yes")
    
    else:
    
        print("no")
    p=0    