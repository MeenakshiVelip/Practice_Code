n=int(input())
arr=[]
for i in range(0,n):
    arr.append(int(input()))
flag=0
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            arr[i]=arr[i]+1
        if arr[j] < 0:
            flag=0
sum=0
for i in range(0,n):
    sum=sum+arr[i]
if flag==1:
    print("Wrong output")
else:
    print(sum)                             