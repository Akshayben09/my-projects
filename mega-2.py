def prime (n):
    if n==1:
        return False
    for i in range (2,n//2+1):
        if (n%i==0):
             return False
    return True
def dp(n):
    while (n):
        r=n%10
        if (r!=2 and r!=3 and r!=5 and r!=7):
             return False
        n=n//10
    return True
def mp(n):
    if (prime(n) and dp(n)):
         return True
    return False
a,b=map(int, input (). split ())
for i in range (a,b+1):
    if (mp(i)):
        print (i, end=' ')