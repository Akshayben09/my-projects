n=int (input ())
count=0
while (n) :
    r=n%10
    count+=1
    print (r)
    n=n//10
print (count)