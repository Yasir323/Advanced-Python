# The AudioPlayer class acts as a context. It also maintains a
# reference to an instance of one of the state classes that
# represents the current state of the audio player.
class UserInterface:
    pass


class Event:
    doubleClick = None


class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)
        self.UI = UserInterface()
        self.volume = None
        self.playlist = None
        self.currentSong = None

        # Context delegates handling user input to a state
        # object. Naturally, the outcome depends on what state
        # is currently active, since each state can handle the
        # input differently.
        self.UI.lockButton.onClick(self.clickLock)
        self.UI.playButton.onClick(self.clickPlay)
        self.UI.nextButton.onClick(self.clickNext)
        self.UI.prevButton.onClick(self.clickPrevious)

    # Other objects must be able to switch the audio player's
    # active state.
    def changeState(self, state):
        self.state = state

    # UI methods delegate execution to the active state.
    def clickLock(self):
        self.state.clickLock()

    def clickPlay(self):
        self.state.clickPlay()

    def clickNext(self):
        self.state.clickNext()

    def clickPrevious(self):
        self.state.clickPrevious()

    # A state may call some service methods on the context.
    def startPlayback(self):
        pass

    def stopPlayback(self):
        pass

    def nextSong(self):
        pass

    def previousSong(self):
        pass

    def fastForward(self, time):
        pass

    def rewind(self, time):
        pass


# The base state class declares methods that all concrete
# states should implement and also provides a backreference to
# the context object associated with the state. States can use
# the backreference to transition the context to another state.
class State:
    def __init__(self, player):
        self.player = player

    def clickLock(self):
        pass

    def clickPlay(self):
        pass

    def clickNext(self):
        pass

    def clickPrevious(self):
        pass


# Concrete states implement various behaviors associated with a
# state of the context.
class LockedState(State):
    def clickLock(self):
        if self.player.playing:
            self.player.changeState(PlayingState(self.player))
        else:
            self.player.changeState(ReadyState(self.player))

    def clickPlay(self):
        pass

    def clickNext(self):
        pass

    def clickPrevious(self):
        pass


# They can also trigger state transitions in the context.
class ReadyState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.startPlayback()
        self.player.changeState(PlayingState(self.player))

    def clickNext(self):
        self.player.nextSong()

    def clickPrevious(self):
        self.player.previousSong()


class PlayingState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.stopPlayback()
        self.player.changeState(ReadyState(self.player))

    def clickNext(self):
        if Event.doubleclick:
            self.player.nextSong()
        else:
            self.player.fastForward(5)

    def clickPrevious(self):
        if Event.doubleclick:
            self.player.previousSong()
        else:
            self.player.rewind(5)
