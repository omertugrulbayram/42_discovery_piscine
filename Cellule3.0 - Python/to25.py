#!/usr/bin/env python3

num = int(input("Enter a number less than 25 : "))

if num > 25:
    print("Too high, enter less than 25.")
else:
    while num <= 25:
        print(num)
        num = num + 1