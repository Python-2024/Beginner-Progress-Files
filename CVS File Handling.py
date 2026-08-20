# Raj is the manager of a medical store. To keep track of sales records, he has created a
# CSV file named Sales.csv, which stores the details of each sale.
# The columns of the CSV file are: Product_ID, Product_Name, Quantity_Sold and
# Price_Per_Unit.
# Help him to efficiently maintain the data by creating the following user-defined functions:
# I. Accept() – to accept a sales record from the user and add it to the file Sales.csv.
# II. CalculateTotalSales() – to calculate and return the total sales based on the
# Quantity_Sold and Price_Per_Unit.

import csv

def accept(file_path):
    with open(file_path, 'a+', newline='') as f:
        detid = eval(input("Enter ID, Name, Quantity, Price: "))
        write = csv.writer(f)
        write.writerow(detid)
        print("Record added successfully.")

def CalculateTotalSales(file_path):
    with open(file_path, 'r') as f1:
        total_sales = 0
        line = csv.reader(f1)
        for row in line:
            if row[3]:
                total_sales += int(row[3]) * float(row[2])
        return total_sales

accept(r'D:\Python files\data.csv')
print("Total Sales: ", CalculateTotalSales(r'D:\Python files\data.csv'))