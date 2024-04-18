v1beta1import csv

# Open the CSV file and read the headers
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    
    # Read each row of the CSV file and print the values for each column
    for row in reader:
        print(row['column1'], row['column2'])
        
        
# function to add 2 numbers
def add_numbers (num1, num2):
    return num1 + num2

# recursive function to get factorial of a number
def getFactorial(n) :
    if n == 0 :
        return 1
    else :
        return n * getFactorial(n-1)
    