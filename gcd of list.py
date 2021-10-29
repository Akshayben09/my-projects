#gcd of two numbers using list and sets
a,b = map(int,input().split())
a_div=[i for i in range(1,a//2+1) if a%2==0]
a_div.append(a)
print(a_div)
b_div=[i for i in range(1,b//2+1) if b%2==0]
b_div.append(b)
print(b_div)
c_div=list(set(a_div).intersection(set(b_div)))
print(max(c_div))
