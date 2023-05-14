arr = [ 1,4,6,8,2]
t = 10
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
       sum= arr[i]+arr[j]
       if sum==t:
          print(arr[i],arr[j])
          #break