def ispalindrome(s):
    rev=''.join(reversed(s))
    if(s==rev):
        return True
    return False
s=input("X=")
a=ispalindrome(s)
if(a):
    print("True")
else:
    print("False")
