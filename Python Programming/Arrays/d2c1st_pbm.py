n=int(input())
t=str(n)
sum=0
for i in t:
    sum=sum+int(i)
print(sum)    
if n%sum==0:
    print("yes")
else:
    print("No")    