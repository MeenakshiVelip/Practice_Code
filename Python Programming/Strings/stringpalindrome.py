n=input()
n=n.casefold()
rev=reversed(n)
if list(n)==list(rev):
    print('palindrome')
else:
    print('not palindrome')    