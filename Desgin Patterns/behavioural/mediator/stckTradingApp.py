"""In a stock trading system, the Mediator pattern can be used to coordinate the communication between various
components, such as traders, stock exchanges, and order matching engines. The mediator facilitates the routing of buy
and sell orders, matches orders, and provides feedback to traders. """


class StockTradingMediator:
    def __init__(self):
        self.traders = []

    def register_trader(self, trader):
        self.traders.append(trader)

    def execute_trade(self, trader, stock, quantity, action):
        # Execute trade logic
        # ...
        pass


class Trader:
    def __init__(self, name, stock_trading_mediator):
        self.name = name
        self.stock_trading_mediator = stock_trading_mediator

    def buy_stock(self, stock, quantity):
        self.stock_trading_mediator.execute_trade(self, stock, quantity, "BUY")

    def sell_stock(self, stock, quantity):
        self.stock_trading_mediator.execute_trade(self, stock, quantity, "SELL")


# Usage
stock_trading_mediator = StockTradingMediator()

trader1 = Trader("John", stock_trading_mediator)
trader2 = Trader("Jane", stock_trading_mediator)
trader3 = Trader("Alice", stock_trading_mediator)

stock_trading_mediator.register_trader(trader1)
stock_trading_mediator.register_trader(trader2)
stock_trading_mediator.register_trader(trader3)

trader1.buy_stock("AAPL", 10)
trader2.sell_stock("GOOGL", 5)
