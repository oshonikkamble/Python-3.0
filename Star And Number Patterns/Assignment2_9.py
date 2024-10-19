def digits(No):
    
    return len(str(No))

def main():
    print(("Enter The number: "))
    A = int(input())

    No = digits(A)
    
    print("Number of digits : ", No)

if __name__ == "__main__":
    main()