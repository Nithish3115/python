# cook your dish here
t=int(input())
f_n=0
s_n=0

for i in range(t):
    k=int(input())
    t=list(map(int,input().split()))
    for j in range(len(t)-1):
        f_n=t[j]
        l_n=t[j+1]
        if(f_n == l_n):
            k=k-1
            
        else:
            k=k+0
    print(k)        
    