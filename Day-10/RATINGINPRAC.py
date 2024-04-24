t = int(input())
l=[]
r=0

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    for j in range(len(d)-1):
        if(d[j]<=d[j+1]):
           r=r+0
        else:
            r=r+1
    if(r>=1):
            print('No')
    else:
            print("yes")
    r=0    
    t -= 1
