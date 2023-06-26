import abc


# The "implementation" interface declares methods common to all
# concrete implementation classes. It doesn't have to match the
# abstraction's interface. In fact, the two interfaces can be
# entirely different. Typically, the implementation interface
# provides only primitive operations, while the abstraction
# defines higher-level operations based on those primitives.
class Device(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "isEnabled") and
                callable(subclass.isEnabled) and
                hasattr(subclass, "enable") and
                callable(subclass.enable) and
                hasattr(subclass, "disable") and
                callable(subclass.disable) and
                hasattr(subclass, "getVolume") and
                callable(subclass.getVolume) and
                hasattr(subclass, "setVolume") and
                callable(subclass.setVolume) and
                hasattr(subclass, "getChannel") and
                callable(subclass.getChannel) and
                hasattr(subclass, "setChannel") and
                callable(subclass.setChannel) or
                NotImplemented)

    def isEnabled(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def getVolume(self):
        raise NotImplementedError

    def setVolume(self, percent: float):
        raise NotImplementedError

    def getChannel(self):
        raise NotImplementedError

    def setChannel(self, channel: str):
        raise NotImplementedError


# The "abstraction" defines the interface for the "control"
# part of the two class hierarchies. It maintains a reference
# to an object of the "implementation" hierarchy and delegates
# all the real work to this object.
class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def togglePower(self):
        if self._device.isEnabled():
            self._device.disable()
        else:
            self._device.enable()

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)

    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)

    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)

    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)


# You can extend classes from the abstraction hierarchy
# independently of device classes.
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.setVolume(0)


# All devices follow the same interface.
class Tv(Device):
    # Implement the methods for TV device here.
    def isEnabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def getVolume(self):
        pass

    def setVolume(self, percent: float):
        pass

    def getChannel(self):
        pass

    def setChannel(self, channel: str):
        pass


class Radio(Device):
    # Implement the methods for Radio device here.
    def isEnabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def getVolume(self):
        pass

    def setVolume(self, percent: float):
        pass

    def getChannel(self):
        pass

    def setChannel(self, channel: str):
        pass


# Somewhere in client code.
tv = Tv()
remote = RemoteControl(tv)
remote.togglePower()

radio = Radio()
remote = AdvancedRemoteControl(radio)
