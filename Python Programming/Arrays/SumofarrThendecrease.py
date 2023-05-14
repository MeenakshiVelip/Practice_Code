n=int(input())
arr = []
sum=0
for i in range (0,n):
    a=int(input())
    arr.append(a)
for i in range(0,n):
    sum=sum+arr[i]
    print(sum)    
for i in range(0,n):
    sum=sum-arr[i]
    print(sum)
