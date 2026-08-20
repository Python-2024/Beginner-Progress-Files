# A) Write a Python function that displays all the words containing @gmail
# from a text file "Emails.txt".
# OR
# B)Write a Python function that finds and displays all the words longer than
# 5 characters from a text file "Words.txt".

def func1():
    with open("D:/Python files/Novel.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().endswith('@gmail.com'):
                print(line.strip())
def func2():
    with open("D:/Python files/Novel.txt", "r") as file2:
        lines1 = file2.readlines()
        for line in lines1:
            l1 = line.strip().split(' ')
            for word in l1:
                if len(word) > 5:
                    print(f'The words which more than 5 charcter are; {word}')
func1()
func2()