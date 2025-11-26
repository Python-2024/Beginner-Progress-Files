number = int(input("enter a number: "))

counter = 0

for i in range(1, number + 1):
    even_num = 2 * i
    print("Even number:", even_num)
    counter += even_num

print("Sum of first", number, "even numbers:", counter)


"""
number = int(input("enter a number: "))

counter = 0

for num in range(1, (number*2) + 1):
    if num%2==0:
        print(f"First {number} even number: ",num)

    counter += num
    print(f"Sum of first {number} even number: ",counter)
"""