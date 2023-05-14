def create_stack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item)
def pop(stack):
    if isempty(stack):
      print("stack is empty")
    stack.pop()
stack=create_stack()
n=int(input("enter size"))
for i in range(0,n):
    item=input("enter item")
    push(stack,str(item))      
#push(stack,str(20))      
#push(stack,str(30))      
#push(stack,str(40))      
#push(stack,str(50))  
print( pop(stack))  
print(str(stack))  