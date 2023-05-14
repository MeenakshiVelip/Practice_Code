#Remove Every Third Element From the List
arr = [ 1,4,6,8,2,5,3]
k=2
idx=0
l=len(arr)
while l>1:
    idx=(k+idx)%l
    print(arr.pop(idx),end=" ")
    l=l-1 
for i in arr:  
   print()     
   print('last element is',i)
