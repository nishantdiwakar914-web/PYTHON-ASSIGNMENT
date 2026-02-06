import os

# Use 'sample.txt' as requested in the homework image
file_name = "sample.txt" 

try:
    # Attempt to open the file in read mode
    with open(file_name, 'r') as file:
        print("Reading file content:")
        # Print content line by line as requested
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    # If the file doesn't exist, this code runs instead
    print(f"Error: The file '{file_name}' was not found.")

