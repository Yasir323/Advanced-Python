"""
Encapsulation is the process of preventing clients from accessing 
certain properties, which can only be accessed through specific 
methods.

Private attributes are inaccessible attributes, and information 
hiding is the process of making particular attributes private. 
You use two underscores to declare private characteristics.

We can see that all the attributes are printed except the 
private attribute __discount. You use getter and setter methods 
to access private attributes.
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


if __name__ == '__main__':
    book1 = Book('Random book', 12, 'Random author', 120)
    print(book1)
    print()
    print(book1.title)
    print(book1.quantity)
    print(book1.author)
    print(book1.price)
    try:
        print(book1.__discount)
    except AttributeError:
        print("Cannot access a private attribute")
    print(book1.get_discount())
    book1.set_discount(0.2)
    print(book1.get_discount())
