from MarvellousNum import *

def listprime(numbers):
    prime_sum = 0
    for num in numbers:
        if ChkPrime(num):
            prime_sum = prime_sum + num
    return prime_sum

def main():
    print("Enter the number of elements: ")
    n = int(input())
    
    A= list()
    print("Numbers : ")

    for i in range(n):
        no=int(input())
        A.append(no)


    print("List of numbers:",A)

    prime_sum = listprime(A)
    print("Sum of prime numbers in the list:", prime_sum)

if __name__ == "__main__":
    main()