#1.multiplication and sum of two numbers
def calculate(num1, num2):
    summation = num1 + num2
    multiplication = num1 * num2
    return summation, multiplication

num1 = 5
num2 = 3
sum_result, multiplication_result = calculate(num1, num2)

print(f"Sum: {sum_result}")
print(f"Multiplication: {multiplication_result}")


#2.declare two variables and print that which variable is largest using ternary operators
a = 10
b = 20

# Using the ternary operator to determine the largest variable
largest = a if a > b else b

# Print the result
print(f"The largest number is: {largest}")

#3.take input from the user (name, age,city)and print it in a formatted string using python
# Taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Printing the formatted string
print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")

import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

#4.find the area of a triangle given its three sides

# Example usage
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Check if the sides form a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    area = calculate_area(side1, side2, side3)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The given sides do not form a valid triangle.")

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Taking user input
num = int(input("Enter a number: "))

# Checking if the number is even or odd
result = check_even_odd(num)

# Printing the result
print(f"The number {num} is {result}.")

# Function to calculate square and cube of a number
def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Input from user
number = float(input("Enter a number: "))

# Call the function and display results
square, cube = calculate_square_and_cube(number)
print(f"The square of {number} is: {square}")
print(f"The cube of {number} is: {cube}")









