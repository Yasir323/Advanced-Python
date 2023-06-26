"""Consider a text editor application where users can perform various operations, such as typing, deleting,
or formatting text. The Command pattern can be used to implement the undo/redo functionality. Each user action can be
encapsulated as a command object, which stores the necessary information to perform and undo the action. The text
editor keeps track of the executed commands and allows users to undo or redo their actions, modifying the document's
state accordingly. """


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.document = ""
        self.command_history = []
        self.current_position = 0

    def execute_command(self, command):
        command.execute()
        self.command_history.append(command)
        self.current_position += 1

    def undo_last_command(self):
        if self.current_position > 0:
            command = self.command_history[self.current_position - 1]
            command.undo()
            self.current_position -= 1

    def redo_last_command(self):
        if self.current_position < len(self.command_history):
            command = self.command_history[self.current_position]
            command.execute()
            self.current_position += 1


class InsertCommand(Command):
    def __init__(self, editor, text, position):
        self.editor = editor
        self.text = text
        self.position = position

    def execute(self):
        self.editor.document = (
                self.editor.document[: self.position]
                + self.text
                + self.editor.document[self.position:]
        )

    def undo(self):
        self.editor.document = (
                self.editor.document[: self.position]
                + self.editor.document[self.position + len(self.text):]
        )


class DeleteCommand(Command):
    def __init__(self, editor, start, end):
        self.editor = editor
        self.start = start
        self.end = end
        self.deleted_text = self.editor.document[self.start: self.end]

    def execute(self):
        self.editor.document = (
                self.editor.document[: self.start] + self.editor.document[self.end:]
        )

    def undo(self):
        self.editor.document = (
                self.editor.document[: self.start]
                + self.deleted_text
                + self.editor.document[self.start:]
        )


# Usage
editor = TextEditor()

insert_command = InsertCommand(editor, "Hello", 0)
delete_command = DeleteCommand(editor, 0, 5)

editor.execute_command(insert_command)
print(editor.document)  # Output: "Hello"

editor.execute_command(delete_command)
print(editor.document)  # Output: ""

editor.undo_last_command()
print(editor.document)  # Output: "Hello"
