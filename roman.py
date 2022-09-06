s = str(input())
s = s.upper()
n = len(s)
ans = 0

for i in range(0,n):
    if(s[i]=='I'):
        ans +=1;
    elif(s[i]=='V'):
        ans += 5;
    elif(s[i]=='X'):
        ans += 10;
    elif(s[i]=='L'):
        ans += 50;
    elif(s[i]=='C'):
        ans += 100;
    elif(s[i]=='D'):
        ans += 500;
    elif(s[i]=='M'):
        ans += 1000;

for i in range(0,n-1):
    if(s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X') ):
        ans -= 2;
    if(s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C') ):
        ans -= 20;
    if(s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M') ):
        ans -= 200;
    
print(ans)











