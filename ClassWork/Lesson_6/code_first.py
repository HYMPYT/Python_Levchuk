big_number = -999999999999999

number = int(input("Enter the number or -1 to close program: "))

while number != -1:
    if number > big_number:
        big_number = number
    number = int(input("Enter the number or -1 to close program: "))

print("The big number: ", big_number)