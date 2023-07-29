n = int(input("enter n"))
que = []
for i in range(n):
    q = int(input("enter element"))
    que.append(q)
print(que)    

# dequeue element from front end
for i in range(n):
    print("Removed element is ", end=" ")
    print(que.pop(0))
    