#!/usr/bin/python3

# Write a program that asks the user to enter three numbers (use three separate input statements). 
# Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average.

a = eval(input("Enter the first number:"))
b = eval(input("Enter the second number:"))
c = eval(input("Enter the third number:"))

total = a + b + c
print ("The total of the three numbers = ", total)
average = total / 3
print ("The average of the three numbers = ", average)
