# arr = [ 1,4,6,8,1,4]
# for i in range(len(arr)):
#     print(i,end=" ")
#     print(arr[i])
arr = [ 1,4,6,8,1,4]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(arr[i])
  
