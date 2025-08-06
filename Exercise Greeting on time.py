"""

Create a python program capable of greeting you with Good Morning,
Good Afternoon and Good Evening. Your program should use time module to get
the current hour.
Here is a sample program and documentation link for you.

"""
# time.strftime("%Y %m %d %H %M %S")


import time

current_time = time.strftime("%H:%M:%S")
print("Current time ", current_time)

current_time = time.strftime("%H%M%S")

#time schedule
morning = "000000"
afternoon = "115959"
evening = "160000"
night = "170000"

#conditions

#moring
if int(morning) <= int(current_time) < int(afternoon):
    print("Good Morning Sir!")
#afternoon
elif int(afternoon) <= int(current_time) < int(evening):
    print("Good Afternoon Sir!")
#evening
elif int(evening) <= int(current_time) < int(night):
    print("Good Evening Sir!")
#night
else:
    print("Good Night Sir!")