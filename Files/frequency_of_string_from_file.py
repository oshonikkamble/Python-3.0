
with open('Demo.txt', 'w') as file:
    file.write("Marvellous Infosystem.")
    file.write("Python Programming at Marvellous.\n")
    file.write("C,C++,Java with Marvellous.\n")
import os
def read_file_and_count_string(filename, search_string):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    with open(filename, 'r') as file:
        fobj = file.read()
    
    frequency = fobj.count(search_string)
    return frequency

print("Enter the name of the file: ")
file_name = input()

print("Enter the string to search for: ")
search_string = input()

frequency = read_file_and_count_string(file_name, search_string)
if frequency is not None:
    print(f'The string "{search_string}" appears {frequency} times in the file "{file_name}".')
