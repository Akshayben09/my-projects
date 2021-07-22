n=int(input ())
rev=0
while (n):
    r=n%10
    rev=rev*10+r
    n=n//10
   
e=0
o=0
while (rev):
    r=rev%10
    if (r%2==0):
         e=e*10+r
    else:
         o=o*10+r
    print (e)
    print (o)