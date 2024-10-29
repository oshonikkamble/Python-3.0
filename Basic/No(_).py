
def Accept(No):
    
    i = 0
    
    if(No <= 0):
        print(" invalid Input ")
        return
    
    while(i < No ):
        print(" * ", end = "")
        i = i + 1

def main():
    print("Enter The Number of * : ")
    No = int(input())
    Accept(No)

if __name__ == "__main__":
    main()
