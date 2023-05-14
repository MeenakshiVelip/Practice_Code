n=int(input())
arr=list(map(int,input().split()))
i=0
while i<len(arr)-1:
  if i==arr[i]:
     t=arr[i]
     arr[i]=arr[i-1]
     arr[i-1]=t
  i=i+1
print(arr)