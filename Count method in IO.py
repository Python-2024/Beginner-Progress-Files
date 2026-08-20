# Write a Python function that counts and returns the number of
# digits appearing in the text file "Space.txt".

def count_digits_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            nwl = line.strip()
            for char in nwl:
                if char.isdigit():
                    count += 1
        print(f"Number of digits in the file: {count}")

count_digits_in_file(r"D:\Python files\Novel.txt")