t = int(input())
first_letter=''
second_letter=''
third_letter=''
vowels=['a','e','i','o','u']
final=0

for i in range(t):
    s=str(input())
    for j in range (len(s)-2):
       first_letter=s[j]
       second_letter=s[j+1]
       third_letter=s[j+2]
       if(first_letter in vowels) and (second_letter in vowels) and( third_letter in vowels):
           if(final<1):
             final= final+1
           else:
                final+=0
       else:
           final=final+0
       first_letter=''
       second_letter=''
       third_letter=''
    if(final):
        print("happy")
    else:
        print("sad")
    final=0    
       
       