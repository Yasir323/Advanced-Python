"""
Suppose you are working with a GUI framework that has its own set of UI widgets. However, you need to use a
different UI library that provides similar functionality but with a different interface. You can create adapters to
wrap the UI widgets of the first framework and expose a common interface that your code expects.
"""


# Existing UI framework with incompatible widgets
class LegacyButton:
    def render_button(self):
        pass

    def handle_click(self):
        pass


# Adapter for LegacyButton
class ButtonAdapter:
    def __init__(self, legacy_button):
        self.legacy_button = legacy_button

    def render(self):
        self.legacy_button.render_button()

    def onclick(self, event):
        self.legacy_button.handle_click()


# Usage
legacy_button = LegacyButton()
button_adapter = ButtonAdapter(legacy_button)
button_adapter.render()
button_adapter.onclick("click event")

"""In this example, the LegacyButton represents a UI widget from an existing GUI framework. The ButtonAdapter class 
acts as an adapter, encapsulating the functionality of the LegacyButton and providing a common interface for 
rendering the button and handling click events. """
