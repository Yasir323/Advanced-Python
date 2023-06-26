"""The Iterator pattern can also be used when reading data from a file or an external data source in a custom way."""


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        return FileIterator(self.file_path)


class FileIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.file is None:
            self.file = open(self.file_path, 'r')
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()


# Usage
file_reader = FileReader('data.txt')

for line in file_reader:
    print(line)
