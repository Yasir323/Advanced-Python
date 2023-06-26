"""Consider a file system where you have different types of entities such as files and directories. The Composite
pattern can be utilized to represent the file system's hierarchical structure, allowing you to treat both individual
files and directories uniformly. You can perform operations like traversing the file system, calculating the total
size of a directory and its subdirectories, or printing the file structure. """


# Component - Abstract base class for file system entities
class FileSystemComponent:
    def get_size(self):
        raise NotImplementedError()

    def display_structure(self, indent=0):
        raise NotImplementedError()

# Leaf - Represents individual files
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display_structure(self, indent=0):
        print('  ' * indent + self.name)

# Composite - Represents directories that can contain other file system entities
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_component(self, component):
        self.children.append(component)

    def remove_component(self, component):
        self.children.remove(component)

    def get_size(self):
        total_size = 0
        for component in self.children:
            total_size += component.get_size()
        return total_size

    def display_structure(self, indent=0):
        print('  ' * indent + self.name + '/')

        for component in self.children:
            component.display_structure(indent + 1)

# Usage
file1 = File('file1.txt', 100)
file2 = File('file2.txt', 50)
file3 = File('file3.txt', 75)

directory1 = Directory('directory1')
directory1.add_component(file1)
directory1.add_component(file2)

directory2 = Directory('directory2')
directory2.add_component(file3)

root_directory = Directory('root')
root_directory.add_component(directory1)
root_directory.add_component(directory2)

print('Total size:', root_directory.get_size())
root_directory.display_structure()

"""In this example, the FileSystemComponent class is the abstract base class for file system entities. The File class 
represents individual files, and the Directory class represents directories that can contain files and 
subdirectories. The Directory class maintains a list of child components and provides methods to calculate the total 
size of the directory and display the file system structure. """
