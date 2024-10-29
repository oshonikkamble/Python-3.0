with open('Demo.txt', 'w') as file:
    file.write("This is the content of Demo.txt.\nIt has multiple lines.\n")

with open('Hello.txt', 'w') as file:

    file.write("This is the content of Demo.txt.\nIt has multiple lines.\n")

import os

def filecontents(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    with open(filename, 'r') as file:
        return file.read()

def comparefiles(file1, file2):

    content1 = filecontents(file1)
    content2 = filecontents(file2)
    
    if content1 is None or content2 is None:
        return
    
    if content1 == content2:
        print("Success: The contents of both files are the same.")
    else:
        print("Failed: The contents of the files are different.")

def main():
    print("Enter the name of the first file: ")
    file1 = input()

    print("Enter the name of the second file: ")
    file2 = input()

    comparefiles(file1, file2)

if __name__ == "__main__":
    main()
