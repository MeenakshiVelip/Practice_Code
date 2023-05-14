def rem(arr):
    k=2
    i=0
    length=(len(arr))
    while length>1:
        i=(i+k)%length
        arr.pop(i)
        length=length-1
        if length==1:
            print(arr)
            
arr=[10,20,30,40]     
print(rem(arr))  