a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    print("a is greater than b and c=")
elif b>a and b>c:
    print("b is greater than both")
elif c>a and c>b:
    print("c is greater than both")  
else:
    print("wrong")          
