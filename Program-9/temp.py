print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")

choice = int(input("Enter Your Choice 1 or 2 : "))
if choice == 1:
    c = float(input("Enter Temp in Celsius : "))
    f = (c * 9/5) + 32
    print(f"Celsius {c} == Fahrenheit {f}")
elif choice == 2:
    f = float(input("Enter Temp in Fahrenheit : "))
    c = (f - 32) * 5/9
    print(f"Fahrenheit {f} == Celsius {c}")
else:
    print("Invalid Choice")