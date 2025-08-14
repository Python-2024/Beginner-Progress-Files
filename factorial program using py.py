#Factorial of n numbers


"""
formula for the factorial is n! = n*(n-1)!
"""

num1 = int(input("Enter the number: "))
r1 = 1
for i in range(1, num1+1):
    r1 *= i
print(r1)