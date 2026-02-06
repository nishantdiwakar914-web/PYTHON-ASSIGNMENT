import os 

file_name = "simple.txt"

with open("simple.txt", "w") as f:
   f.write("Reading the file content:\n")
   f.write("Line:- This is a sample text file.\n")
   f.write("Line: It contains multiple lines\n")

if os.path.exists(file_name):

    print("simple.txt")

else:
    print("Error: The", file_name "was not found.")
