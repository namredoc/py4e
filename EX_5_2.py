largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        int_num = int(num)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = int_num

    if smallest > int_num:
        smallest = int_num

    if largest is None:
        largest = int_num

    if largest < int_num:
        largest = int_num



print("Maximum is", largest)
print("Minimum is", smallest)