class Bookstore:
    NoOfBooks = 0

    def __init__(self,name,writer):
        self.Name = name
        self.Writer = writer
        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1

    def display(self):
        print(f"{self.Name} by {self.Writer}. No Of Books : {Bookstore.NoOfBooks}")

obj1=Bookstore("Linux System Programming","Robert Love")
obj1.display()
obj2=Bookstore("C Programming","Dennis Ritchie")
obj2.display()
