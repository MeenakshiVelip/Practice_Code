arr = [2,4,8,46,24,56,16]
n=len(arr)
k=2
s=set(arr)
print(s)
for i in s:
    if k==1:
        print(i)
        break
    k=k-1
