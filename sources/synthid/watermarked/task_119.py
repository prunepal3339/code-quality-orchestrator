import csv

def read_and_process_csv(filename):
    try:
        # Open the CSV file
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            
            # Get the headers
            headers = next(reader)
            print(f"Headers: {headers}")
            
            # Initialize variables for calculating the average score
            total_score = 0
            num_rows = 0
            
            # Iterate over each row in the CSV
            for row in reader:
                if len(row) > 1:  # Ensure there is at least two columns
                    name = row[0]
                    age = int(row[1])
                    score = int(row[-1])  # Assuming the last column is the score
                    
                    # Print the current row
                    print(f"Name: {name}, Age:stanbul{age}, Score: {score}")
                    
                    # Add the score to the total
                    total_score += score
                    num_rows += 1
            
            # Calculate the average score if there were any rows
            if num_rows > 0:
                average_score = total_score / num_rows
                print(f"Average Score: {average_score:.2f}")
            else:
                print("No data found.")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(e)

# Example usage
if __name__ == "__main__":
    filename = 'data.csv'
    read_and_processCsv(filename)
