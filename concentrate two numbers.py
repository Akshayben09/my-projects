'''concaterate two numbers is
a=12.  b=56
a*10**dc+b
12*10**2+56=1256
dc=digit count of b'''


a,b=map(int, input (). split ())
t=b
dc=0
while (b):
    b=b//10
    dc+=1
r=a*10**dc+t
print (r)
