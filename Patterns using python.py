"""
This program gives you the pattern (*)
"""

#user input
num1 = int(input("Enter the number: "))
r1 = 1
#loop
for i in range(1, num1+1):
    r1 *= i
    i *= "*" #numbers convert into strings
    print(i)

"""
Here, this is the secound program in this this will give you both of the factorial and pattern number.
"""

num2 = int(input("\n\nEnter the number: "))
r2 = 1
star = "*"
#lopp fun.
for i in range(1, num2+1):
    r2 *= i #factorial
    print(f"{i}! = {r2}  {star * i}") #formula used here

"""
Recursive star pattern :)
"""
print("\n\n")
a = int(input("Enter the number: "))
r3 = 1
while a>=r3:
    g = "*" * (a-r3)
    print(g)
    r3 += 1

"""
This program will print the Pyramid structure pattern
"""
print("\n\n")

b = int(input("Enter the number: "))
i = 1
#loop
while b >= i:
    #condition for space and stars
    space = " " * (b-i)
    stars = "*" * (2*i - 1)
    #accurating the condition for pyramid pattern
    print(space + stars)
    #for not infinite loop
    i += 1

"""
Diamond patter using python
"""
print("\n\n")

#numbers and reference
n = 10
r = 1
#Straight Pyramid
while n >= r:
    down_space = " " * (n-r)
    if r % 2 != 0:
        c =down_space + (2*r-1)*"*"
        print(c)
    r+=1 #for finite loop

#Reversed Pyramid
n = 10
r = 1
while n >= r:
    reverse2 = (n-r)
    up_space2 = " " * r
    if reverse2 % 2 != 0:
        d = up_space2 + (2*reverse2-1)*"*"
        print(d)
    else:
        pass
    r += 1