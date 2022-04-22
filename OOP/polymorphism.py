"""
The term 'polymorphism' comes from the Greek language and 
means 'something that takes on multiple forms.'

Polymorphism refers to a subclass's ability to adapt a method 
that already exists in its superclass to meet its needs. To 
put it another way, a subclass can use a method from its 
superclass as is or modify it as needed.
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
    def __init__(self, title, quantity, author, price, genre):
        super().__init__(title, quantity, author, price)
        self.genre = genre


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
    
    def __repr__(self) -> str:
        return f"Book: {self.title}\nBranch: {self.branch}\nQuantity: {self.quantity}\nAuthor: {self.author}\nPrice: {self.price}"


if __name__ == '__main__':
    book1 = Book('Random book', 12, 'Random author', 120)
    novel1 = Novel('Two States', 20, 'CB', 200, 'Fiction')
    academic1 = Academic('Intro to OS', 30, 'Skiena', 800, 'IT')
    print(book1)
    print()
    print(novel1)
    print()
    print(academic1)
