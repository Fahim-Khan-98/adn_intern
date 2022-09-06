n = int(input())

if (n==1):
    print(n)
elif (n==2):
    print(n)
else:
    
    a = 1
    b = 2
    for i in range(3,n):
        
        c = a+b
        a=b
        b=c
print(a+b)

        
        
        
        