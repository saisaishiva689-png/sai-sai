a = int(input("Enter the value of a = "))
b = int(input("Enter  the value of b = "))
op = input("Enter the operator (+,-,*,/) = ")
if op == '+' :
    print("Sum of the two numbers = ",a+b)
elif op == '-' :
    print("Sub of the two numbers = ",a-b)
elif  op == '*' :
    print("Mul of the two numbers = ",a*b)
elif op == '/' :
    if b == 0 :
        print("B can not be zero")
    else:
        print("Div of  two numbers = ",a/b)
else :
    print("Invaild Input")