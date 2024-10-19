
import threading
import time


def thread1():
    print("Execution of Thread 1 : ")
    for i in range(1, 51):
        print(i)
        time.sleep(0.1)  


def thread2():
    print("Execution of Thread 2 : ")
    for i in range(50, 0, -1):    
        print(i)
        time.sleep(0.1)  
    

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t1.join()  
t2.start()
t2.join()  

print("Both threads completed execution.")