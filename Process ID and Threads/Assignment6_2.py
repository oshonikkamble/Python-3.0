
import os
import threading

def Evenfactor(No):
    
    print("PID of Even Process " , os.getpid())
    print("PID of Even Thread ", threading.get_ident())
    
    print("List Of Even Numbers : ")
    s = 0
    for i in range(1, No+1):    
        if (No % i == 0):
            print(i)

            if (i % 2 == 0):
                s = s+i  
                
    print("Addition of Even Factors : ",s)
       
def Oddfactor(No):

    print("PID of Odd Process " , os.getpid())
    print("PID of Odd Thread ", threading.get_ident())
    
    print("List Of Odd Numbers : ")
    x = 0
    for i in range(1, No+1):    
        if (No % i == 0):
            print(i)    

            if (i %2 != 0):
                x = x + i
    
    print("Addition of all Oddfactor : ",x)

def main():

    print("PID Of Main Process " , os.getpid())
    print("PID Of Main Thread " , threading.get_ident())

    print("Enter Number: ")
    A=int(input())

    p1 = threading.Thread(target = Evenfactor ,args =(A ,))
    p2 = threading.Thread(target = Oddfactor ,args = (A ,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print("Exit from main process")

if __name__ == "__main__":
    main()
