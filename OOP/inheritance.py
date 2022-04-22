"""
Inheritance is regarded as the most significant characteristics 
of OOP. A class's ability to inherit methods and/or 
characteristics from another class is known as inheritance.

The subclass or child class is the class that inherits. The 
superclass or parent class is the class from which methods 
and/or attributes are inherited.
"""


class Book:
    def __init__(self, title, quantity, author, price) -> None:
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = 0.10

    def __repr__(self) -> str:
        return f"Book: {self.title}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.price}"

    def set_discount(self, discount):
        self.__discount = discount
    
    def get_discount(self):
        return str(self.__discount * 100) + '%'


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


if __name__ == '__main__':
    book1 = Book('Random book', 12, 'Random author', 120)
    novel1 = Novel('Two States', 20, 'CB', 200, 187)
    academic1 = Academic('Intro to OS', 30, 'Skiena', 800, 'IT')
    print(book1)
    print()
    print(novel1)
    print()
    print(academic1)
