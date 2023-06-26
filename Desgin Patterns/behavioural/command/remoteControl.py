"""Consider a scenario where you have a remote control that can operate different electronic devices,
such as a television, sound system, and lights. The Command pattern can be used to implement the remote control
functionality. Each device operation, such as turning on/off or changing the volume, can be encapsulated as a command
object. The remote control stores a collection of these command objects, and when a button is pressed,
the corresponding command is executed. This allows for flexible configuration of the remote control and easy addition
of new devices or commands. """


class Command:
    def execute(self):
        pass


class Television:
    def turn_on(self):
        print("TV turned on.")

    def turn_off(self):
        print("TV turned off.")


class SoundSystem:
    def volume_up(self):
        print("Volume up.")

    def volume_down(self):
        print("Volume down.")


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if button in self.commands:
            self.commands[button].execute()


# Usage
tv = Television()
sound_system = SoundSystem()

tv_on_command = Command(lambda: tv.turn_on())
tv_off_command = Command(lambda: tv.turn_off())
volume_up_command = Command(lambda: sound_system.volume_up())
volume_down_command = Command(lambda: sound_system.volume_down())

remote = RemoteControl()
remote.set_command("A", tv_on_command)
remote.set_command("B", tv_off_command)
remote.set_command("X", volume_up_command)
remote.set_command("Y", volume_down_command)

remote.press_button("A")  # Turns on the TV
remote.press_button("X")  # Increases the volume
