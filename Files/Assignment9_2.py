import os

def main():

    print("Enter name of the file you want Display their content")
    fname = input()

    if os.path.exists(fname):
        fobj = open(fname,"r")
        print("File is Successfully open")

        print("Contents in File : ")
        Data=fobj.read()
        print(Data)

        fobj.close()
    else:
        print("Unable to open file as not prsent in dictionary")

if __name__ == "__main__":
    main()
