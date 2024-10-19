def Addition(No):
    
    sum = 1
    
    for i in range(2, int(No**0.5) + 1):
        if (No % i == 0):
            sum = sum +  i  # it can also write as sum += i
            if (i != No // i):
              sum = sum + (No // i)  # it can also write as sum += No // i
    
    return sum

def main():
    
    print("Enter The number: ")
    A = int(input())
    
    sum = Addition(A)
    print("Addition of factors: ", sum)

if __name__ == "__main__":
    main()