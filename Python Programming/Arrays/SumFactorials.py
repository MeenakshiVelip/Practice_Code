n=int(input())
fact=1
res=0
for i in range(1,n+1):
    fact=fact*i
print(fact)    
while fact!=0:
    lastdigit = fact%10
    res=res+lastdigit
    fact=fact//10
print(res)    