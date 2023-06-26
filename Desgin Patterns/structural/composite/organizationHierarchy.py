"""Suppose you are working on a human resources system that manages an organization's hierarchy. The Composite
pattern can be applied to represent the organizational structure, where each employee can be treated as an individual
or as a manager who can have subordinates. This pattern allows you to perform operations on individual employees or
groups of employees, such as calculating the total salary, printing the organization chart, or identifying the
hierarchy. """


# Component - Abstract base class for employees
class Employee:
    def get_salary(self):
        raise NotImplementedError()

    def display_hierarchy(self, indent=0):
        raise NotImplementedError()


# Leaf - Represents individual employees
class IndividualEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display_hierarchy(self, indent=0):
        print('  ' * indent + self.name)


# Composite - Represents managers who can have subordinates
class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        self.subordinates.remove(subordinate)

    def get_salary(self):
        total_salary = self.salary
        for subordinate in self.subordinates:
            total_salary += subordinate.get_salary()
        return total_salary

    def display_hierarchy(self, indent=0):
        print('  ' * indent + self.name)

        for subordinate in self.subordinates:
            subordinate.display_hierarchy(indent + 1)


# Usage
individual1 = IndividualEmployee('John', 5000)
individual2 = IndividualEmployee('Alice', 4000)
individual3 = IndividualEmployee('Bob', 3000)

manager1 = Manager('Manager1', 10000)
manager1.add_subordinate(individual1)
manager1.add_subordinate(individual2)

manager2 = Manager('Manager2', 8000)
manager2.add_subordinate(individual3)

ceo = Manager('CEO', 20000)
ceo.add_subordinate(manager1)
ceo.add_subordinate(manager2)

print('Total salary:', ceo.get_salary())
ceo.display_hierarchy()

"""In this example, the Employee class is the abstract base class for employees. The IndividualEmployee class 
represents individual employees, while the Manager class represents managers who can have subordinates. The Manager 
class maintains a list of subordinates and provides methods to calculate the total salary and display the 
organizational hierarchy. """
