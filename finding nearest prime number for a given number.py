def prime(n):
    if n==1:
        return False
    for i in range (2,n//2+1):
        if (n%i==0):
            return False
    return True
n=int(input ())
if (prime(n)):
    print (n)
else:
    a=n+1
    while (True):
       if (prime(a)):
           h=a
           break
       a+=1
    b=n-1
    while (True):
        if (prime(b)):
            l=b
            break
        b-=1
    if n-l < h-n:
         print (l)
    elif h-n < n-l:
         print (h)
    else:
         print (h,l)