n = int(input("enter n"))
stack = []
for i in range(n):
    s = int(input("enter element"))
    stack.append(s)
print(stack)    

# POP element
for i in range(n):
    print("Poped element is ", end=" ")
    print(stack.pop())
    