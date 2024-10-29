

def prime(No):
    
    if No > 1:
        for i in range(2, No):
            if (No % i) == 0:
                
                print("is not a prime number")
                break
        else:
            print( "is a prime number")

    else:   
        print("is not a prime number")

def main():
    print("Enter The Number : ")
    A=int(input())

    prime(A)

if __name__ == "__main__":
    main()
