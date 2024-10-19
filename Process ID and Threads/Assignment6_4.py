import os
import threading

def small(str):
    print("PID of Small Character " ,os.getpid())
    print("TID of Small Character" ,threading.get_ident())

    s=0
    for i in str:
        if(i >= 'a' and i <= 'z'):
            s = s + 1
    print("Number of Small character : " , s )

def capital(str):
    print("PID of Capital Character " ,os.getpid())
    print("TID of Capital Character" ,threading.get_ident())
    
    c=0
    for i in str:
        if(i >= 'A' and i <= 'Z'):
            c = c + 1
    
    print("Number of Capital character : " , c )

def digit(str):
    print("PID of Digit ",os.getpid())
    print("TID of Digit ",threading.get_ident())

    d = 0
    for c in str:
        if c.isdigit():
            d = d + 1
        else:
            pass

    print("Number of Digits : ", d)

def main():

    print("PID of Main Process" ,os.getpid())
    print("PID of Main Thread" ,threading.get_ident())

    print("Enter String: ")
    str=input()

    p1=threading.Thread(target = small,args=(str, ))
    p2=threading.Thread(target = capital,args=(str, ))
    p3=threading.Thread(target = digit,args=(str,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()

if __name__ == "__main__":
    main()