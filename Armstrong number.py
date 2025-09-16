#Arm- strong number of digit 3
#153 = 1^3 + 5^3 + 3^3 = 153
#370 = 3^3 + 7^3 + 0^3 = 370
#_______________________________________________________________________________________________________________________

#old code
number = str(input("Enter a number: ")).strip()
power = int(input("Enter a power: "))
r = 0

for i in number:
    r += int(i)**power
print(r)



#_______________________________________________________________________________________________________________________


#here this is the updated code
while True:
    number = str(input("Enter a number: ")).strip()
    power = len(number)

    r = 0
    for i in number:
        r += int(i)**power
    print(r)
