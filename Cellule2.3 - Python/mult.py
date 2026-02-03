#!/usr/bin/env python3

ilk = input("Enter the first number: ")
iki = input("Enter the second number: ")
carp = int(ilk) * int(iki)
print("The multiplication of the two numbers is: " + str(carp))

if carp > 0:
    print("The result is a positive number.")
if carp < 0:
    print("The result is a negative number.")
else:
    print("The result is zero.")   