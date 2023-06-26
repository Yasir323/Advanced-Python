# The component interface defines operations that can be
# altered by decorators.
class DataSource:
    def writeData(self, data):
        raise NotImplementedError

    def readData(self):
        raise NotImplementedError


# Concrete components provide default implementations for the
# operations. There might be several variations of these
# classes in a program.
class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def writeData(self, data):
        # Write data to file.
        pass

    def readData(self):
        # Read data from file.
        pass


# The base decorator class follows the same interface as the
# other components. The primary purpose of this class is to
# define the wrapping interface for all concrete decorators.
# The default implementation of the wrapping code might include
# a field for storing a wrapped component and the means to
# initialize it.
class DataSourceDecorator(DataSource):
    def __init__(self, source):
        self.wrappee = source

    # The base decorator simply delegates all work to the
    # wrapped component. Extra behaviors can be added in
    # concrete decorators.
    def writeData(self, data):
        self.wrappee.writeData(data)

    # Concrete decorators may call the parent implementation of
    # the operation instead of calling the wrapped object
    # directly. This approach simplifies extension of decorator
    # classes.
    def readData(self):
        return self.wrappee.readData()


# Concrete decorators must call methods on the wrapped object,
# but may add something of their own to the result. Decorators
# can execute the added behavior either before or after the
# call to a wrapped object.
class EncryptionDecorator(DataSourceDecorator):
    def writeData(self, data):
        # 1. Encrypt passed data.
        # 2. Pass encrypted data to the wrappee's writeData
        # method.
        pass

    def readData(self):
        # 1. Get data from the wrappee's readData method.
        # 2. Try to decrypt it if it's encrypted.
        # 3. Return the result.
        pass


# You can wrap objects in several layers of decorators.
class CompressionDecorator(DataSourceDecorator):
    def writeData(self, data):
        # 1. Compress passed data.
        # 2. Pass compressed data to the wrappee's writeData
        # method.
        pass

    def readData(self):
        # 1. Get data from the wrappee's readData method.
        # 2. Try to decompress it if it's compressed.
        # 3. Return the result.
        pass


# Option 1. A simple example of a decorator assembly.
class Application:
    def dumbUsageExample(self):
        source = FileDataSource("somefile.dat")
        source.writeData(salaryRecords)
        # The target file has been written with plain data.

        source = CompressionDecorator(source)
        source.writeData(salaryRecords)
        # The target file has been written with compressed
        # data.

        source = EncryptionDecorator(source)
        # The source variable now contains this:
        # Encryption > Compression > FileDataSource
        source.writeData(salaryRecords)
        # The file has been written with compressed and
        # encrypted data.


# Option 2. Client code that uses an external data source.
# SalaryManager objects neither know nor care about data
# storage specifics. They work with a pre-configured data
# source received from the app configurator.
class SalaryManager:
    def __init__(self, source):
        self.source = source

    def load(self):
        return self.source.readData()

    def save(self):
        self.source.writeData(salaryRecords)
    # ...Other useful methods...


# The app can assemble different stacks of decorators at
# runtime, depending on the configuration or environment.
class ApplicationConfigurator:
    def configurationExample(self):
        source = FileDataSource("salary.dat")
        if enabledEncryption:
            source = EncryptionDecorator(source)
        if enabledCompression:
            source = CompressionDecorator(source)

        logger = SalaryManager(source)
        salary = logger.load()
    # ...
