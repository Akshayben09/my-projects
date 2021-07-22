n=int (input ())
sum=0
while (n) :
    r=n%10
    sum+=r
    print (r)
    n=n//10
print (sum)