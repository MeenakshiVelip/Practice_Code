n=int(input())
def count_digit(n):
    if n<10:
        return n
    elif n/10 < 10:
        return 9
    elif n/100 < 10:
        return 9 + n - 99 
    elif n/1000 < 10:
        return 9 + 900
    elif n/10000 < 10:
        return 909 + n - 9999
    else:
        return 90909
print(count_digit(n))                      
