#user input
a = int(input("A) Enter the 1st number: "))
b = int(input("B) Enter the 2st number: "))
c = int(input("C) Enter the 3st number: "))

#bigger conditions
if a>b and a>c:
    print("\nA is greater")
elif b>a and b>c:
    print("\nB is greater")
else:
    print("\nC is greater")

#smaller conditions
if a<b and a<c:
    print("\nA is smaller")
elif b<a and b<c:
    print("\nB is smaller")
else:
    print("\nC is smaller")
