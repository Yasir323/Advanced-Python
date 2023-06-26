# The strategy interface declares operations common to all
# supported versions of some algorithm. The context uses this
# interface to call the algorithm defined by the concrete
# strategies.
class Strategy:
    def execute(self, a, b):
        pass


# Concrete strategies implement the algorithm while following
# the base strategy interface. The interface makes them
# interchangeable in the context.
class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b


# The context defines the interface of interest to clients.
class Context:
    def __init__(self):
        self.strategy = None

    # Usually the context accepts a strategy through the
    # constructor, and also provides a setter so that the
    # strategy can be switched at runtime.
    def set_strategy(self, strategy):
        self.strategy = strategy

    # The context delegates some work to the strategy object
    # instead of implementing multiple versions of the
    # algorithm on its own.
    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)


# The client code picks a concrete strategy and passes it to
# the context. The client should be aware of the differences
# between strategies in order to make the right choice.
class ExampleApplication:
    def main(self):
        # Create context object.
        context = Context()

        # Read first number.
        first_number = int(input("Enter the first number: "))

        # Read last number.
        last_number = int(input("Enter the last number: "))

        # Read the desired action from user input.
        action = input("Enter the desired action (addition/subtraction/multiplication): ")

        if action == "addition":
            context.set_strategy(ConcreteStrategyAdd())
        elif action == "subtraction":
            context.set_strategy(ConcreteStrategySubtract())
        elif action == "multiplication":
            context.set_strategy(ConcreteStrategyMultiply())
        else:
            print("Invalid action.")

        result = context.execute_strategy(first_number, last_number)

        print("Result:", result)


# Create an instance of ExampleApplication and run the main method.
app = ExampleApplication()
app.main()
