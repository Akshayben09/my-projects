def prime(n) :
    if n==1 :
        return False
    for i in range (2,n//2+1):
        if (n%2==0):
             return False
        return True
n=int (input ())
if prime(n):
    print ('prime')
else:
    print ("not prime")