# Calculate the sum of n numbers using a loop.

#user input
user_input = int(input("Enter the number: "))
#Ref. point
r_sum = 0
#loop
for i in range(1,user_input+1):
    r_sum += i
print(r_sum)