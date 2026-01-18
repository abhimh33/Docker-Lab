number = int(input("Enter a number : "))
def fact(number):
    if number == 0 or number == 1:
        return 1
    return number * fact(number - 1)
print(f"Factorial of {number} is : {fact(number)}")