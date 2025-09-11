print("Use 'q' for quiet")

r = 0 #initial value
while True:
    num = input("Enter a number: ")
    if num.isdigit(): #validate for the integer value
        r = r + int(num)

    if num.lower() == "q": #validate for the string value
        print("The total number is {}".format(r))
        break
        #end of the program