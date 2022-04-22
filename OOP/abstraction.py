"""
Abstraction isn't supported directly in Python. Calling a 
magic method, on the other hand, allows for abstraction.

If an abstract method is declared in a superclass, subclasses 
that inherit from the superclass must have their own 
implementation of the method.

A superclass's abstract method will never be called by its subclasses. But the abstraction aids in the maintenance of a similar structure across all subclasses.

In our parent class Book, we have defined the __repr__ method. 
Let's make that method abstract, forcing every subclass to 
compulsorily have its own __repr__ method.
"""
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price) -> None:
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = 0.10

    @abstractmethod
    def __repr__(self) -> str:
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.price}"

    def set_discount(self, discount):
        self.__discount = discount
    
    def get_discount(self):
        return str(self.__discount * 100) + '%'


class Novel(Book):
    def __init__(self, title, quantity, author, price, genre):
        super().__init__(title, quantity, author, price)
        self.genre = genre


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
    
    def __repr__(self) -> str:
        return f"Book: {self.title}\nBranch: {self.branch}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.price}"


try:
    book1 = Book('Random book', 12, 'Random author', 120)
except Exception as e:
    print(f"{type(e).__name__}: {str(e)}")
academic1 = Academic('Intro to OS', 30, 'Skiena', 800, 'IT')
print(academic1)
print()
try:
    novel1 = Novel('Two States', 20, 'CB', 200, 'Fiction')
    print(novel1)
except Exception as e:
    print(f"{type(e).__name__}: {str(e)}")


class Novel(Book):
    def __init__(self, title, quantity, author, price, genre):
        super().__init__(title, quantity, author, price)
        self.genre = genre
    
    def __repr__(self) -> str:
        return f"Book: {self.title}\nGenre: {self.genre}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.price}"


novel1 = Novel('Two States', 20, 'CB', 200, 'Fiction')
print(novel1)