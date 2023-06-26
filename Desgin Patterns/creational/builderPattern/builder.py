from abc import ABC, abstractmethod


# Using the Builder pattern makes sense only when your products
# are quite complex and require extensive configuration. The
# following two products are related, although they don't have
# a common interface.
class Car:
    # A car can have a GPS, trip computer and some number of
    # seats. Different models of cars (sports car, SUV,
    # cabriolet) might have different features installed or
    # enabled.
    pass


class Manual:
    # Each car should have a user manual that corresponds to
    # the car's configuration and describes all its features.
    pass


# The builder interface specifies methods for creating the
# different parts of the product objects.
class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self, seats):
        pass

    @abstractmethod
    def setEngine(self, engine):
        pass

    @abstractmethod
    def setTripComputer(self, trip_computer):
        pass

    @abstractmethod
    def setGPS(self, gps):
        pass


# The concrete builder classes follow the builder interface and
# provide specific implementations of the building steps. Your
# program may have several variations of builders, each
# implemented differently.
class CarBuilder(Builder):
    def __init__(self):
        self.car = None
        self.reset()

    def reset(self):
        self.car = Car()

    def setSeats(self, seats):
        # Set the number of seats in the car.
        pass

    def setEngine(self, engine):
        # Install a given engine.
        pass

    def setTripComputer(self, trip_computer):
        # Install a trip computer.
        pass

    def setGPS(self, gps):
        # Install a global positioning system.
        pass

    def getProduct(self):
        product = self.car
        self.reset()
        return product


# Unlike other creational patterns, builder lets you construct
# products that don't follow the common interface.
class CarManualBuilder(Builder):
    def __init__(self):
        self.manual = None
        self.reset()

    def reset(self):
        self.manual = Manual()

    def setSeats(self, seats):
        # Document car seat features.
        pass

    def setEngine(self, engine):
        # Add engine instructions.
        pass

    def setTripComputer(self, trip_computer):
        # Add trip computer instructions.
        pass

    def setGPS(self, gps):
        # Add GPS instructions.
        pass

    def getProduct(self):
        # Return the manual and reset the builder.
        return self.manual


class SportEngine:
    pass


# The director is only responsible for executing the building
# steps in a particular sequence. It's helpful when producing
# products according to a specific order or configuration.
# Strictly speaking, the director class is optional, since the
# client can control builders directly.
class Director:
    # The director works with any builder instance that the
    # client code passes to it. This way, the client code may
    # alter the final type of the newly assembled product.
    # The director can construct several product variations
    # using the same building steps.
    @staticmethod
    def constructSportsCar(builder, num_seats):
        builder.reset()
        builder.setSeats(num_seats)
        builder.setEngine(SportEngine())
        builder.setTripComputer(True)
        builder.setGPS(True)

    def constructSUV(self, builder):
        # ...
        pass


# The client code creates a builder object, passes it to the
# director, and then initiates the construction process. The end
# result is retrieved from the builder object.
class Application:
    @staticmethod
    def makeCar():
        director = Director()

        car_builder = CarBuilder()
        director.constructSportsCar(car_builder, 2)
        car = car_builder.getProduct()

        manual_builder = CarManualBuilder()
        director.constructSportsCar(manual_builder, 2)

        # The final product is often retrieved from a builder
        # object since the director isn't aware of and not
        # dependent on concrete builders and products.
        manual = manual_builder.getProduct()
