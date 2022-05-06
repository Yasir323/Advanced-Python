"""As we might expect, this principle states that a class should only have one responsibility. Furthermore,
it should only have one reason to change. How does this principle help us to build better software? Let's see a few
of its benefits:

Testing – A class with one responsibility will have far fewer test cases.
Lower coupling – Less functionality in a single class will have fewer dependencies.
Organization – Smaller, well-organized classes are easier to search than monolithic ones.
"""
import _io


class Book:

    name: str
    author: str
    text: str

    def __init__(self):
        pass

    def replace_word_in_text(self, old_word: str, new_word: str) -> str:
        return self.text.replace(old_word, new_word)

    def is_word_in_text(self, word: str) -> int:
        return self.text.find(word)


"""
Now our Book class works well, and we can store as many books as we like in our application.

But what good is storing the information if we can't output the text to our console and read it?

However, we must not implement that method in this class, we should implement a separate one.
"""


class BookPrinter:

    @staticmethod
    def print_text_to_console(self, text: str):
        print(text)

    @staticmethod
    def print_text_to_file(self, text: str, fp: _io.TextIOWrapper):
        print(text, file=fp)
