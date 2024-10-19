
def Pattern(No):
    
    for i in range(No):
        for j in range(No):
            
            print(j + 1, end=" ")
        
        print()

def main():
    
    print("Enter The Number : ")
    No = int(input())

    Pattern(No)

if __name__ == "__main__":
    main()   