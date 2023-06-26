"""When working with file operations, such as reading, writing, and manipulating files, you can use a File Operations
Facade to provide a simplified interface. The facade can encapsulate the underlying complexities of file handling and
provide high-level methods that clients can use without dealing with the low-level details. """

import os


class FileFacade:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def delete_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"File '{self.file_path}' deleted.")
        else:
            print(f"File '{self.file_path}' does not exist.")


# Usage
facade = FileFacade("example.txt")
facade.write_file("Hello, World!")
content = facade.read_file()
print("File Content:", content)
facade.delete_file()

"""In this example, the FileFacade encapsulates the file operations of reading, writing, and deleting a file. Clients 
can use the facade methods (read_file(), write_file(), and delete_file()) to perform these operations without 
worrying about the low-level file handling details. """
