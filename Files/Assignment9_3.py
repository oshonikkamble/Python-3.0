import os

def main():
    print("Enter Frst File name that you want to read : ")
    fname=input()

    print("Enter Second file name that you want copy the contents From first file :")
    fname2 = input()

    fobj = open(fname,"r")
    print("File is successfully opened in read mode")
        
    fobj2 = open(fname2,"w")
    for line in fobj:
            
        fobj2.write(line)
    print("Contents From File 1 Copied Successfully")

if __name__ == "__main__":
    main()