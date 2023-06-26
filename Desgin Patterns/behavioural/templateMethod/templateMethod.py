from abc import ABC, abstractmethod


# The abstract class defines a template method that contains a
# skeleton of some algorithm composed of calls, usually to
# abstract primitive operations. Concrete subclasses implement
# these operations but leave the template method itself intact.
class GameAI(ABC):
    # The template method defines the skeleton of an algorithm.
    def turn(self):
        self.collectResources()
        self.buildStructures()
        self.buildUnits()
        self.attack()

    # Some of the steps may be implemented right in a base class.
    def collectResources(self):
        for s in self.builtStructures:
            s.collect()

    # And some of them may be defined as abstract.
    @abstractmethod
    def buildStructures(self):
        pass

    @abstractmethod
    def buildUnits(self):
        pass

    # A class can have several template methods.
    def attack(self):
        enemy = self.closestEnemy()
        if enemy is None:
            self.sendScouts(map.center)
        else:
            self.sendWarriors(enemy.position)

    @abstractmethod
    def sendScouts(self, position):
        pass

    @abstractmethod
    def sendWarriors(self, position):
        pass


# Concrete classes have to implement all abstract operations of
# the base class but they must not override the template method
# itself.
class OrcsAI(GameAI):
    def buildStructures(self):
        if self.areSomeResources():
            # Build farms, then barracks, then stronghold.
            pass

    def buildUnits(self):
        if self.arePlentyOfResources():
            if not self.areScouts():
                # Build peon, add it to scouts group.
                pass
            else:
                # Build grunt, add it to warriors group.
                pass

    def sendScouts(self, position):
        if len(self.scouts) > 0:
            # Send scouts to position.
            pass

    def sendWarriors(self, position):
        if len(self.warriors) > 5:
            # Send warriors to position.
            pass


# Subclasses can also override some operations with a default
# implementation.
class MonstersAI(GameAI):
    def collectResources(self):
        # Monsters don't collect resources.
        pass

    def buildStructures(self):
        # Monsters don't build structures.
        pass

    def buildUnits(self):
        # Monsters don't build units.
        pass


# Create instances of the concrete classes and use them accordingly.

# Example usage of OrcsAI
orcs_ai = OrcsAI()
orcs_ai.turn()

# Example usage of MonstersAI
monsters_ai = MonstersAI()
monsters_ai.turn()
