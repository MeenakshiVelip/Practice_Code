# arr = list(map(int,input("enter elements").split()))
# print(arr)
def Peak(arr,n):
  if len(arr)==1:
    return 0
  if(arr[0]>=arr[1]):
    return 0
  if(arr[n-1]>=arr[n-2]):
    return n-1
  for i in range(1,n-1):
    if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
      return arr[i]
    
arr = list(map(int,input("enter elements").split()))
print(arr)
print(Peak(arr,len(arr)))