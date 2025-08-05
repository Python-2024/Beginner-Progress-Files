# # Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())


str1 = "Hi Hi Hi! How are you all?"
print(str1.rsplit("?"))

print(str1.find("How"))

print(str1.replace("Hi", "What's up homies"))

print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.swapcase())

print(str1.count("Hi"))

print(str1.find("gjg"))
print(str1.find("H"))

print(str1.index("How"))

str2 = "To kill a Mocking bird"
print(str2.istitle())

print(str2.title())

print(str2.capitalize())

print(str2.split(" "))

print(str2.startswith("To"))
print(str2.endswith("Bird"))

print("\n")
str3 = "  "       #using Tab
print(str3.isspace())
print(str2.isprintable())

print(str1.center(50))