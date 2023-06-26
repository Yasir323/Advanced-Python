"""Imagine you are developing a GUI framework, and you need to represent different UI components such as windows,
buttons, labels, and panels. The Composite pattern can be applied to create a hierarchical structure for GUI
components. Each component, whether it's a leaf (e.g., a button or a label) or a composite (e.g., a panel that
contains multiple components), can be treated uniformly. You can perform operations such as rendering,
handling events, or manipulating the entire UI structure consistently. """


# Component - Abstract base class for GUI components
class Component:
    def render(self):
        raise NotImplementedError()


# Leaf - Represents individual GUI components
class Button(Component):
    def render(self):
        print("Render button")


class Label(Component):
    def render(self):
        print("Render label")


# Composite - Represents composite GUI components that can contain other components
class Panel(Component):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def render(self):
        print("Render panel")

        for component in self.components:
            component.render()


# Usage
button1 = Button()
button2 = Button()
label = Label()

panel = Panel()
panel.add_component(button1)
panel.add_component(button2)
panel.add_component(label)

panel.render()
"""In this example, the Component class is the abstract base class for GUI components, and Button and Label are leaf 
nodes representing individual components. The Panel class is the composite node that can contain multiple components. 
The Panel class maintains a list of child components and recursively renders each component. """
