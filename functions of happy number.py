def is_happy(n):
  while n!=1 and n!=4:
     ss=0
     while (n):
        r=n%10
        ss+=r*r
        n=n//10
     n=ss
  if n==1:
      return True
  else:
      return False
while (True):
  x=input ("check or range")
  if (x=='check') :
     num=int(input ("enter a number to check:"))
     if (is_happy(num)):
        print ("happy number")
     else:
        print ("unhappy number")
  elif (x=='range'):
     a,b=map (int, input ("enter two numbers:"). split ())
     choose=input ("happy number or unhappy number??")
     if (choose=="happy number"):
        for i in range (a,b+1):
          if (is_happy(i)):
            print (i, end=' ')
          else:
            for i in range (a,b+1):
              if (not is_happy(i)):
                 print (i, end=' ')
  else:
     print ("invalid input")