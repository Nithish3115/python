# cook your dish here
t=int(input())
k=''
for i in range(t):
    n=str(input())
    for j in n[-1::-1]:
        k= k+ j
    if(k== n):
            print("wins")
    else:
            print("loses")
            
    # print(k)
    k=''
        
        