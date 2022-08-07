number = float(input("Enter the number, please: "))

if number < 0.0 or number > 1:
    print("Error: The number is out of range.")
    quit()

elif number >= 0.9:
    print("A")
elif number >= 0.8:
    print("B")
elif number >=0.7:
    print("C")
elif number >= 0.6:
    print("D")
elif number < 0.6:
    print("F")