"""Suppose you are developing a GUI framework that supports multiple platforms such as Windows, macOS, and Linux,
and you want to provide different UI implementations for each platform. By using the Bridge pattern, you can separate
the GUI framework's abstraction (e.g., Window, Button, Label) from the platform-specific UI implementations (e.g.,
WindowsUI, MacOSUI, LinuxUI). This allows you to independently evolve the GUI framework and UI implementations. """


# Abstraction - Window
class Window:
    def __init__(self, ui_implementation):
        self.ui_implementation = ui_implementation

    def draw(self):
        self.ui_implementation.draw_window()


# Implementations - UI Implementations for different platforms
class UIImplementation:
    def draw_window(self):
        pass


class WindowsUI(UIImplementation):
    def draw_window(self):
        print("Drawing a window in Windows style")


class MacOSUI(UIImplementation):
    def draw_window(self):
        print("Drawing a window in macOS style")


class LinuxUI(UIImplementation):
    def draw_window(self):
        print("Drawing a window in Linux style")


# Usage
windows_ui = WindowsUI()
window = Window(windows_ui)
window.draw()

macos_ui = MacOSUI()
window = Window(macos_ui)
window.draw()

linux_ui = LinuxUI()
window = Window(linux_ui)
window.draw()

"""In this example, the Window class represents the abstraction in the GUI framework. The UIImplementation is the 
implementation hierarchy that provides the different UI styles for each platform. By using the Bridge pattern, 
you can create different instances of the Window class with different UI implementations, allowing the GUI framework 
to adapt to various platforms. """
