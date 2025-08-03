#welcoming
print("Welcome to the calculator!\n")

#user options
print("choose what do you want;\nAdd, Sub or Multiplication\n")
user = str(input("Enter your choice: \n")).lower()
#user input 
a = int(input("Enter your first number: "))
b = int(input("Enter your secound number: "))

#conditions
add = a + b 
sub = a - b
multi = a * b
if user == str("add"):
    print(add)
elif user == str("sub"):
    print(sub)
else:
    print(multi)