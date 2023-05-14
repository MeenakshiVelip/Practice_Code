#arr=[1,2,3,4]
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)//2):
    t= arr[i]
    arr[i]=arr[len(arr)-i-1]
    arr[len(arr)-i-1]=t
print(arr)    
