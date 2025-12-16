#!/usr/bin/env python3

# Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average.

num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter another number: "))
num3 = eval(input("another he third number: "))

total = num1 + num2 + num3
average = total / 3

print("Total:", total, "Average:", average, sep=" ")
