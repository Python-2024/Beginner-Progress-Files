a = eval(input("Input: "))
val0 = a[0]
s =0
min_val = []
max_val = []

for i in range(1, len(a)):
    if a[i] < val0:
        min_val.append(a[i])
    elif a[i] > val0:
        max_val.append(a[i])

print("Min: ", min_val)
print("Max: ", max_val)

for j in a:
    s += j
print("Average number ", s/len(a))