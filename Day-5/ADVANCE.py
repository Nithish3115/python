# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x<=y<=(x+200)):
        print("yes")
    else:
        print("no")