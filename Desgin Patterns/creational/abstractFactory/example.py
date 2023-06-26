"""
Suppose you are building a GUI library that needs to support different
operating systems (e.g., Windows, macOS, Linux) with their respective UI
components. You can use the Abstract Factory pattern to create families of
UI components for each operating system.
"""


class Button:
    def render(self):
        raise NotImplementedError()


class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows button...")


class MacOSButton(Button):
    def render(self):
        print("Rendering a macOS button...")


class LinuxButton(Button):
    def render(self):
        print("Rendering a Linux button...")


class Checkbox:
    def render(self):
        raise NotImplementedError()


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a Windows button...")


class MacOSCheckbox(Checkbox):
    def render(self):
        print("Rendering a macOS button...")


class LinuxCheckbox(Checkbox):
    def render(self):
        print("Rendering a Linux button...")


class GUIFactory:
    def create_button(self):
        raise NotImplementedError()

    def create_checkbox(self):
        raise NotImplementedError()


class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSGUIFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


class LinuxGUIFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def render_ui(self):
        self.button.render()
        self.checkbox.render()


class ApplicationConfigurator:
    def __init__(self, conf):
        self.config = conf
        self.start_app()

    def start_app(self):
        if self.config["OS"] == "Windows":
            _factory = WindowsGUIFactory()
        elif self.config["OS"] == "Mac":
            _factory = MacOSGUIFactory()
        elif self.config["OS"] == "Mac":
            _factory = LinuxGUIFactory()
        else:
            raise Exception("Error! Unknown operating system.")
        app = Application(_factory)
        app.create_ui()
        app.render_ui()


config = {"OS": "Linux"}
appConf = ApplicationConfigurator(config)
# Usage
# factory = WindowsGUIFactory()
# button = factory.create_button()
# checkbox = factory.create_checkbox()
# button.render()
# checkbox.render()
