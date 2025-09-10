#Arm- strong number of digit 3
#153 = 1^3 + 5^3 + 3^3 = 153
#370 = 3^3 + 7^3 + 0^3 = 370
#__________________________________


number = str(input("Enter a number: ")).strip()
power = int(input("Enter a power: "))
r = 0

for i in number:
    r += int(i)**power
print(r)
