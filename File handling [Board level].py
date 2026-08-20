# A. Write a Python function that displays the number of times the word "Python"
# appears in a text file named "Prog.txt".

def func():
    with open(file='D:\\Python files\\Novel.txt', mode='r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            nwl = line.strip()
            count += nwl.count('Python')
    print(f'The word "Python" appears {count} times in the file.')

func()