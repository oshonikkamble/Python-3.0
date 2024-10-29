import os

def main():
    print("-- Enter the File you want to create --")
    fname = input()

    if os.path.exists(fname):
        print("File is Already Exists")
    else:
        open(fname,"x")
        print("File is Created")

if __name__ == "__main__":
    main()
