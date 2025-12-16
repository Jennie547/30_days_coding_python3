#!/usr/bin/env python3

 # A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included.
 
print("Welcome, dear customer. You are encouraged to pay a tip 0.0.15 per cent of all you buy (not each).")

price = eval(input("How much is everything?  "))
tip = price * 0.05

print("You will now be charged", price + tip, sep=" ")

