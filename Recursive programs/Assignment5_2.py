i = 1
def DisplayR(No):

    global i

    if(i<= No):
        print(i , end=" ")
        i = i+1
        DisplayR(No)
        

def main():

    print("Enter The number: ")
    No= int(input())
    DisplayR(No)


if __name__ == "__main__":
    main()