def calci():
    a = float(input("Enter a First Number (a) : "))
    b = float(input("Enter a Second Number (b) : "))
    operation = input("Choose an Operation (+,-,*,/) : ")
    if operation == '+':
        print(f"{a} + {b} is : {a+b}")
    elif operation == '-':
        print(f"{a} - {b} is : {a-b}")
    elif operation == '*':
        print(f"{a} * {b} is : {a*b}")
    elif operation == '/':
        if(b == 0):
            print("Can't devide a number by Zero : ")
        else:
            print(f"{a} / {b} is : {a/b}")
    else:
        print("Invalid Entry..!!, Choose Correct Option")
calci()