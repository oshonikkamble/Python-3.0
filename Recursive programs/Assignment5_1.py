i = 1
def DisplayR(No):

    global i

    if(i<= No):
        print( " * ", end=" ")
        i = i+1
        DisplayR(No)
        

def main():

    print("Enter The Number of * : ")
    No= int(input())
    DisplayR(No)


if __name__ == "__main__":
    main()