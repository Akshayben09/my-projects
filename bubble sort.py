#bubble sort
l = list(map(int,input().split()))
n=len(l)
for i in range(n):
    swapped = False
    for j in range(n-1-i):
        if (l[j]>l[j+1]):
            l[j],l[j+1] = l[j+1],l[j]
            swapped = True
    if (swapped == False):
        break
print(l)
