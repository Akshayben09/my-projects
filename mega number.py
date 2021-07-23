def prime(n) :
    if n==1 :
        return False
    for i in range (2,n//2+1):
        if (n%i==0):
             return False
    return True
def dp(n):
    while (n):
        r=n%10
        if (prime(r)):
            pass
        else:
            return False
        n=n//10
    return True
def mp(n):
    if (prime(n) and dp(n)):
        return True
    return False
n=int(input())
if (mp(n)):
   print ('mega')
else:
   print ('not a maga ')