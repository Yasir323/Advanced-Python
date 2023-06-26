"""In GUI development, the Flyweight pattern can be used to optimize the memory usage of graphical widgets,
such as buttons, labels, or icons, that have similar properties. Instead of creating a new object for each widget,
you can share the common properties (e.g., appearance, font, icon) among multiple instances. This reduces memory
overhead and facilitates efficient rendering. """


class WidgetFactory:
    def __init__(self):
        self.widgets = {}

    def get_widget(self, widget_type):
        if widget_type not in self.widgets:
            self.widgets[widget_type] = Widget(widget_type)
        return self.widgets[widget_type]


class Widget:
    def __init__(self, widget_type):
        self.widget_type = widget_type

    def render(self):
        print(f"Rendering {self.widget_type} widget...")


# Usage
factory = WidgetFactory()

widget1 = factory.get_widget("Button")
widget1.render()  # Renders: Rendering Button widget...

widget2 = factory.get_widget("Label")
widget2.render()  # Renders: Rendering Label widget...

widget3 = factory.get_widget("Button")
widget3.render()  # Renders: Rendering Button widget...
