
def Pattern(No):
    
    for i in range(No):
        
        for j in range(No):
            
            print("*", end=" ")
        
        print()

def main():
    
    print("Enter The Number of * : ")
    No = int(input())

    Pattern(No)

if __name__ == "__main__":
    main()   