class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []  # Stack

    def add_text(self, text):
        self.text += text

    def save_snapshot(self):
        snapshot = TextSnapshot(self.text)
        self.history.append(snapshot)

    def undo(self):
        if self.history:
            snapshot = self.history.pop()
            self.text = snapshot.get_text()

    def print_text(self):
        print(self.text)


class TextSnapshot:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text


# Usage
editor = TextEditor()

editor.add_text("Hello, ")
editor.save_snapshot()  # Save state

editor.add_text("world!")
editor.save_snapshot()  # Save state

editor.print_text()  # Output: Hello, world!

editor.undo()  # Undo last change
editor.print_text()  # Output: Hello,

editor.undo()  # Undo again
editor.print_text()  # Output: (empty)
