import csv

# Open the CSV file
with open('example.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file and print it
    for row in csvreader:
        print(row)
