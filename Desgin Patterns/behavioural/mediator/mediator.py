# The mediator interface declares a method used by components
# to notify the mediator about various events. The mediator may
# react to these events and pass the execution to other
# components.
class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError


# The concrete mediator class. The intertwined web of
# connections between individual components has been untangled
# and moved into the mediator.
class AuthenticationDialog(Mediator):
    def __init__(self):
        self.__title = ""
        self.__loginOrRegisterChkBx = Checkbox(self)
        self.__loginUsername = Textbox(self)
        self.__loginPassword = Textbox(self)
        self.__registrationUsername = Textbox(self)
        self.__registrationPassword = Textbox(self)
        self.__registrationEmail = Textbox(self)
        self.__okBtn = Button(self)
        self.__cancelBtn = Button(self)

    # When something happens with a component, it notifies the
    # mediator. Upon receiving a notification, the mediator may
    # do something on its own or pass the request to another
    # component.
    def notify(self, sender, event):
        found = False  # Temp
        if sender == self.__loginOrRegisterChkBx and event == "check":
            if self.__loginOrRegisterChkBx.checked:
                self.__title = "Log in"
                # 1. Show login form components.
                # 2. Hide registration form components.
            else:
                self.__title = "Register"
                # 1. Show registration form components.
                # 2. Hide login form components

        if sender == self.__okBtn and event == "click":
            if self.__loginOrRegisterChkBx.checked:
                # Try to find a user using login credentials.
                if not found:
                    # Show an error message above the login field.
                    pass
            else:
                # 1. Create a user account using data from the
                # registration fields.
                # 2. Log that user in.
                # ...
                pass


# Components communicate with a mediator using the mediator
# interface. Thanks to that, you can use the same components in
# other contexts by linking them with different mediator
# objects.
class Component:
    def __init__(self, dialog):
        self.dialog = dialog

    def click(self):
        self.dialog.notify(self, "click")

    def keypress(self):
        self.dialog.notify(self, "keypress")


# Concrete components don't talk to each other. They have only
# one communication channel, which is sending notifications to
# the mediator.
class Button(Component):
    pass


class Textbox(Component):
    pass


class Checkbox(Component):
    def check(self):
        self.dialog.notify(self, "check")
    # ...
