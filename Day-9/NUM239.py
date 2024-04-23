# # cook your dish here
t=int(input())
num=0
k=['2','3','9']
for i in range(t):
    l,r=map(int,input().split())
    for (j) in range(l,r+1):
      j=str(j)
      if j in k:
          num=num+1
      else:
          if(len(j)>= 2):
            
              o=(j)[len(j)-1]
              if o in k:
                  
                num=num+1
              else:
                  num=num
          else:
                num=num
    print(num) 
    num=0



 
 