def pattern(No):
    i= 1
    while (i <= No) :
        j = 1
        while (j <= i):
            print(j, end = " ")
            
            j =j + 1
        
        print()
        i =i + 1

def main():

    print("Enter Number : ")
    No = int(input())
    
    pattern(No)

if __name__ == "__main__":
    main()