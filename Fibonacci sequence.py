n=int (input ())
a=0
b=1
print (a,b, end=' ')
while (True) :
    c=a+b
    if (c>n-2) :
        break
    print (c, end=' ')
    a=b
    b=c
