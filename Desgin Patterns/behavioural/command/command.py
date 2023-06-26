# The base command class defines the common interface for all
# concrete commands.
class Command:
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    # Make a backup of the editor's state.
    def saveBackup(self):
        self.backup = self.editor.text

    # Restore the editor's state.
    def undo(self):
        self.editor.text = self.backup

    # The execution method is declared abstract to force all
    # concrete commands to provide their own implementations.
    # The method must return True or False depending on whether
    # the command changes the editor's state.
    def execute(self):
        pass


# The concrete commands go here.
class CopyCommand(Command):
    # The copy command isn't saved to the history since it
    # doesn't change the editor's state.
    def execute(self):
        self.app.clipboard = self.editor.getSelection()
        return False


class CutCommand(Command):
    # The cut command does change the editor's state, therefore
    # it must be saved to the history. And it'll be saved as
    # long as the method returns True.
    def execute(self):
        self.saveBackup()
        self.app.clipboard = self.editor.getSelection()
        self.editor.deleteSelection()
        return True


class PasteCommand(Command):
    def execute(self):
        self.saveBackup()
        self.editor.replaceSelection(self.app.clipboard)
        return True


# The undo operation is also a command.
class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False


# The global command history is just a stack.
class CommandHistory:
    def __init__(self):
        self.history = []

    # Last in...
    def push(self, c):
        self.history.append(c)

    # ...first out
    def pop(self):
        if self.history:
            return self.history.pop()


# The editor class has actual text editing operations. It plays
# the role of a receiver: all commands end up delegating
# execution to the editor's methods.
class Editor:
    def __init__(self):
        self.text = ""

    def getSelection(self):
        # Return selected text.
        pass

    def deleteSelection(self):
        # Delete selected text.
        pass

    def replaceSelection(self, text):
        # Insert the clipboard's contents at the current
        # position.
        pass


# The application class sets up object relations. It acts as a
# sender: when something needs to be done, it creates a command
# object and executes it.
class Application:
    def __init__(self):
        self.clipboard = ""
        self.editors = []
        self.activeEditor = None
        self.history = CommandHistory()

    # The code which assigns commands to UI objects may look
    # like this.
    def createUI(self):
        # ...
        copy = lambda: self.executeCommand(CopyCommand(self, self.activeEditor))
        copyButton.setCommand(copy)
        shortcuts.onKeyPress("Ctrl+C", copy)

        cut = lambda: self.executeCommand(CutCommand(self, self.activeEditor))
        cutButton.setCommand(cut)
        shortcuts.onKeyPress("Ctrl+X", cut)

        paste = lambda: self.executeCommand(PasteCommand(self, self.activeEditor))
        pasteButton.setCommand(paste)
        shortcuts.onKeyPress("Ctrl+V", paste)

        undo = lambda: self.executeCommand(UndoCommand(self, self.activeEditor))
        undoButton.setCommand(undo)
        shortcuts.onKeyPress("Ctrl+Z", undo)

    # Execute a command and check whether it has to be added to
    # the history.
    def executeCommand(self, command):
        if command.execute():
            self.history.push(command)

    # Take the most recent command from the history and run its
    # undo method. Note that we don't know the class of that
    # command. But we don't have to, since the command knows
    # how to undo its own action.
    def undo(self):
        command = self.history.pop()
        if command is not None:
            command.undo()
