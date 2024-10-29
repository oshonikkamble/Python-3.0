class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.balance = 0
        self.name = 0
        
    def deposit(self):
        print("----- Welcome To Bank ---- ")
        print("")

        print("-- Enter Your Name --")
        Name = input()
        self.name = Name

        print("-- Enter Money to Deposit --")
        Money=float(input())
        
        self.balance = self.balance + Money
        print("-- Your Amount Deposit --",Money)

    def withdraw(self):
        print()
        print("-- Enter Money To Withdraw -- ")
        Money=float(input())
        if self.balance >= Money:
            self.balance -= Money
            print("-- Money Withdraw --",Money)
        else:
            print("-- Balance is Less --")

    def display(self):
        print()
        print("----- Information -----")
        print("-- Name is --",self.name)
        print("-- Your Balance is --",self.balance)

    def intrest(self):
        print()
        print("-- Principal Amount --",self.balance)
        print("-- Time Period --")
        Time = float(input())

        si = (self.balance * Time * BankAccount.ROI) / 100
        
        print("-- Intrest is --",si)
        return si

obj = BankAccount()
obj.deposit()
obj.withdraw()
obj.display()
obj.intrest()
