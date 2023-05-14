arr=[10,20,30,40,50,60]
#def removeAlternate(arr):
k=3-1
indx=0
l=len(arr)
while l>0 :
	indx=(indx+k)%l
	print(l.pop(indx))
	l=l-1
#arr=[10,20,30,40,50,60]
print(arr)
		
#n = int(input())
#arr=[]
#for i in range(1,n+1):
#    arr.append(i)
#print(removeAlternate(arr))



