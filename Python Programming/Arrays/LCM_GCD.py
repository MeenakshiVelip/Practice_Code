def comp_gcd(x,y):
    while (y):
        x,y=y,x%y
    return x 
def comp_lcm(x,y):
    lcm=(x*y)//comp_gcd(x,y)
    return lcm
n1=int(input())
n2=int(input())   
print('LCM :',comp_lcm(n1,n2))
print('GCD :',comp_gcd(n1,n2))                     