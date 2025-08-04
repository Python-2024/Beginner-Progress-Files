# Checks the following conditions:
#
# If age is less than 13, print "You're a child!"
#
# If age is between 13 and 19 (inclusive), print "You're a teenager!"
#
# Else, print "You're an adult!"

user_age = int(input("Enter your age: "))

if user_age <= 13:
    print("You are a child!")
elif user_age >= 13 and user_age <=19:
    print("you are a teenager!")
else:
    print("You are an adult!")