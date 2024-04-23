# cook your dish here
t=int(input())
s_c=0
l_c=0
s='START38'
la='LAST108'
for i in range(t):
    n=int(input())
    l=list(map(str,input().split()))
    for j in l:
        if(j==s):
            s_c +=1
        else:
            l_c +=1
    print(s_c,l_c)
    s_c=0
    l_c=0
    