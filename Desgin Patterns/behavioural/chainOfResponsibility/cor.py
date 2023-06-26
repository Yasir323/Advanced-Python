# The handler interface declares a method for executing a
# request.
class ComponentWithContextualHelp(metaclass=abc.ABCMeta):
    def showHelp(self):
        raise NotImplementedError


# The abstract base class for simple components.
class Component(ComponentWithContextualHelp):
    def __init__(self):
        self.tooltipText = None
        self._container = None

    # The component's container acts as the next link in the
    # chain of handlers.
    def showHelp(self):
        if self.tooltipText is not None:
            # Show tooltip.
            print("Showing tooltip:", self.tooltipText)
        elif self._container is not None:
            self._container.showHelp()


# Containers can contain both simple components and other
# containers as children. The chain relationships are
# established here. The class inherits showHelp behavior from
# its parent.
class Container(Component):
    def __init__(self):
        super().__init__()
        self.children = []

    def add(self, child):
        self.children.append(child)
        child._container = self


# Primitive components may be fine with default help
# implementation...
class Button(Component):
    pass


# But complex components may override the default
# implementation. If the help text can't be provided in a new
# way, the component can always call the base implementation
# (see Component class).
class Panel(Container):
    def __init__(self):
        super().__init__()
        self.modalHelpText = None

    def showHelp(self):
        if self.modalHelpText is not None:
            # Show a modal window with the help text.
            print("Showing modal window with help text:", self.modalHelpText)
        else:
            super().showHelp()


# ...same as above...
class Dialog(Container):
    def __init__(self):
        super().__init__()
        self.wikiPageURL = None

    def showHelp(self):
        if self.wikiPageURL is not None:
            # Open the wiki help page.
            print("Opening wiki help page:", self.wikiPageURL)
        else:
            super().showHelp()


# Client code.
class Application:
    # Every application configures the chain differently.
    def createUI(self):
        dialog = Dialog()
        dialog.wikiPageURL = "http://..."
        panel = Panel()
        panel.modalHelpText = "This panel does..."
        ok = Button()
        ok.tooltipText = "This is an OK button that..."
        cancel = Button()
        # ...
        panel.add(ok)
        panel.add(cancel)
        dialog.add(panel)

    # Imagine what happens here.
    def onF1KeyPress(self):
        component = self.getComponentAtMouseCoords()
        component.showHelp()
