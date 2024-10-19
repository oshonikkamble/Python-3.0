i=1

def DisplayR(No):

    global i

    if(No>=1):
        print(No , end=" ")
        No = No-1
        DisplayR(No)
        

def main():

    print("Enter The Number: ")
    No= int(input())
    DisplayR(No)


if __name__ == "__main__":
    main()