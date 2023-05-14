n=int(input())
k=int(input())
arr=[]
ind=[]
for i in range(1,n+1):
    arr.append(int(i))
print(arr)
for i in arr:
    ind=arr.index(i)
    print(ind)
while len(arr)>1:
  for i in arr:
    arr.remove(ind[k])  
    if ind[i]==6:
      ind[i]=ind[0] 
print(arr)      
   
 


