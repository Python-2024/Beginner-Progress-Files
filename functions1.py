def palindrome(number):
    if isinstance(number, (int, str)):
        number = str(number)
        if number == number[::-1]:
            print("The number is palindrome")
        else:
            print("The number is not palindrome")
palindrome(56)
palindrome(98)
palindrome(55)


def average(a, b):
    ave = (a + b) / 2
    return ave
average(50, 20)
average(555.66895, 289.55545)