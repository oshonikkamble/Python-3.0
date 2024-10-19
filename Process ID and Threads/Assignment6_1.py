import os
import threading

def Even(No):
    
    print("PID of Even Process " , os.getpid())  
    print("PID of Even Thread " ,threading.get_ident())
    
    print("List Of Even Numbers : ")
    x=2
    for i in range(1,No):
        print(x)
        x = x + 2

def Odd(No):

    print("PID of Even Process " , os.getpid())
    print("PID of Even Thread ", threading.get_ident())
    
    print("List Of Odd Numbers : ")
    x=1
    for i in range(1,No):
        print(x)
        x = x + 2

def main():

    print("PID Of Main Process " , os.getpid())
    print("PID Of Main Thread " , threading.get_ident())

    print("Enter Number: ")
    A=int(input())

    p1 = threading.Thread(target = Even ,args =(A ,))
    p2 = threading.Thread(target = Odd ,args = (A ,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

if __name__ == "__main__":
    main()