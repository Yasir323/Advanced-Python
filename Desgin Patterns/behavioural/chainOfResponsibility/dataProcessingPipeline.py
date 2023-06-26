"""The Chain of Responsibility pattern can be applied to create a data processing pipeline, where each handler
performs a specific processing step on the data. Each handler in the chain can modify or process the data in a
particular way before passing it to the next handler. This approach allows for flexible and reusable data processing
workflows, where different handlers can be combined and rearranged to achieve the desired outcome. """


class DataProcessor:
    def __init__(self, successor=None):
        self.successor = successor

    def process_data(self, data):
        pass


class DataValidationHandler(DataProcessor):
    def process_data(self, data):
        if self.validate_data(data):
            print("Data is valid.")
        elif self.successor is not None:
            self.successor.process_data(data)

    def validate_data(self, data):
        # Perform data validation logic
        return True  # or False


class DataTransformationHandler(DataProcessor):
    def process_data(self, data):
        transformed_data = self.transform_data(data)
        if self.successor is not None:
            self.successor.process_data(transformed_data)

    def transform_data(self, data):
        # Perform data transformation logic
        transformed_data = data
        return transformed_data


# Usage
data = None
data_processor = DataValidationHandler(DataTransformationHandler())
data_processor.process_data(data)
