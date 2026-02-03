#!/usr/bin/env python3

number = int(input("Enter a number:"))
i = 0
while i <= 9:
    result = number * i
    print(str(number) + " x " +  str(i) + " = " + str(result))
    i = i + 1