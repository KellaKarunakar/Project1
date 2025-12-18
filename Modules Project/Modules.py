#This file will acts as a module. It is possible to import this module in the another file. 

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False 
    else:
        return True 
    

def isarmstrong(n):
    s=0 
    t=n 
    while n:
        d=n%10 
        s=s+d**3 
        n=n//10 
    if s==t:
        return True 
    return False 

def ispalindrome(n):
    r=0 
    t=n 
    while n:
        d=n%10 
        r=r*10+d 
        n=n//10 
    if r==t:
        return True 
    return False 

def isperfect(n):
    s=0 
    for i in range(1,n):
        if n%i==0:
            s=s+i 
    if s==n:
        return True
    return False 