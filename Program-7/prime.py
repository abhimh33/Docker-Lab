num = int(input("Enter a number : "))

def prime(num):
    if num <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2,num):
            if num % i == 0:
                print("Not a Prime Number")
                break
        else:
                print(f"{num} is a Prime Number")
prime(num)