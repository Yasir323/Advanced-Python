"""Imagine you have an application that interacts with the file system using a specific library or module. However,
you want to switch to a different file system library without modifying the existing code that relies on the original
library's interface. You can create an adapter that conforms to the original interface but internally uses the new
file system library. """


# Existing file system library with incompatible interface
class LegacyFileSystem:
    def open_file(self, file_path):
        pass

    def read_file(self, file_handle):
        pass

    def close_file(self, file_handle):
        pass


# Adapter for LegacyFileSystem
class FileSystemAdapter:
    def __init__(self, legacy_file_system):
        self.legacy_file_system = legacy_file_system

    def open(self, file_path):
        return self.legacy_file_system.open_file(file_path)

    def read(self, file_handle):
        return self.legacy_file_system.read_file(file_handle)

    def close(self, file_handle):
        self.legacy_file_system.close_file(file_handle)


# Usage
legacy_fs = LegacyFileSystem()
fs_adapter = FileSystemAdapter(legacy_fs)
file_handle = fs_adapter.open("example.txt")
content = fs_adapter.read(file_handle)
fs_adapter.close(file_handle)

"""In this example, the LegacyFileSystem represents the original file system library with its own interface. The 
FileSystemAdapter class acts as an adapter, allowing the code to interact with the file system using the original 
interface while internally delegating the operations to the LegacyFileSystem. """
