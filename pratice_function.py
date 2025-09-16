# Write a function named add_numbers(a, b) that takes two numbers as
# parameters and prints their sum.
# Call the function with values 5 and 7.


def sumofnumber(a, b):
    add = a+b
    print(add)
sumofnumber(5,7)


# Write a function named square(n) that returns the square of a number.
# Call the function with the argument 4 and print the result.

def square_num(a = 4):
    print(a**2)
square_num()

# Write a function factorial(n) that returns the factorial of a number using a
# for loop (factorial of n = n × (n-1) × ... × 1).
# Print the factorial of 5.

def factorial(n):
    r = 1
    for i in range(n,0,-1):
        r *= i
    print(r)
factorial(5)


# Write a function multiply_list(numbers) that takes a list of numbers and returns the product of all numbers in the list.

def multiply_of_the_list(i):
    r = 1
    for j in i:
        r *= int(j)
    print(r)
multiply_of_the_list(i=input("use space b/w every number.\nEnter the number you want to multiply: ").split())


#What is the output of this code? Predict before running:

def func(x):
    return x * 2

print(func(5)) # output: 10
print(func(0)) # output: 0
print(func(-3)) # output: -6
print(func(100)) #output: 200

# Write a function named subtract_numbers(a, b) that takes two numbers as parameters and returns their
# difference (a - b).
# --> Then, store the result in a variable called result1 and print:
# "Difference is: result1"

def subtract(a, b):
    return (a-b)
print(subtract(5,9))


# Write a function named cube(n) that takes a number as input and returns the cube of that number
# (n³).
# 👉 Then, call the function with number 3, store the result in result2, and print:
# "Cube of 3 is: result2"

def cube_numer(n):
    return pow(n,3)
print(cube_numer(5))