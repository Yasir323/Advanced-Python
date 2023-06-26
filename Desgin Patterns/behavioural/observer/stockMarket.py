class StockMarket:
    def __init__(self):
        self.stock_price = None
        self.observers = []

    def set_stock_price(self, price):
        self.stock_price = price
        self.notify_observers()

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.stock_price)


class StockDisplay:
    def __init__(self):
        self.stock_price = None

    def update(self, price):
        self.stock_price = price
        self.display()

    def display(self):
        print(f"Stock price: {self.stock_price}")


# Usage
stock_market = StockMarket()

display1 = StockDisplay()
display2 = StockDisplay()

stock_market.register_observer(display1)
stock_market.register_observer(display2)

stock_market.set_stock_price(100.0)
# Output:
# Stock price: 100.0
# Stock price: 100.0

stock_market.unregister_observer(display2)

stock_market.set_stock_price(105.0)
# Output:
# Stock price: 105.0
