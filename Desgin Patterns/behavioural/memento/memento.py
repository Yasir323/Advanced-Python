# The originator holds some important data that may change over
# time. It also defines a method for saving its state inside a
# memento and another method for restoring the state from it.
class Editor:
    def __init__(self):
        self.__text = ""
        self.__curX = 0
        self.__curY = 0
        self.__selectionWidth = 0

    def setText(self, text):
        self.__text = text

    def setCursor(self, x, y):
        self.__curX = x
        self.__curY = y

    def setSelectionWidth(self, width):
        self.__selectionWidth = width

    # Saves the current state inside a memento.
    def createSnapshot(self):
        # Memento is an immutable object; that's why the
        # originator passes its state to the memento's
        # constructor parameters.
        return Snapshot(self, self.__text, self.__curX, self.__curY, self.__selectionWidth)


# The memento class stores the past state of the editor.
class Snapshot:
    def __init__(self, editor, text, curX, curY, selectionWidth):
        self.__editor = editor
        self.__text = text
        self.__curX = curX
        self.__curY = curY
        self.__selectionWidth = selectionWidth

    # At some point, a previous state of the editor can be
    # restored using a memento object.
    def restore(self):
        self.__editor.setText(self.__text)
        self.__editor.setCursor(self.__curX, self.__curY)
        self.__editor.setSelectionWidth(self.__selectionWidth)


# A command object can act as a caretaker. In that case, the
# command gets a memento just before it changes the
# originator's state. When undo is requested, it restores the
# originator's state from a memento.
class Command:
    def __init__(self, editor):
        self.editor = editor
        self.__backup = None

    def makeBackup(self):
        self.__backup = self.editor.createSnapshot()

    def undo(self):
        if self.__backup is not None:
            self.__backup.restore()
    # ...
