class Object:
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3


class ObjectBuilder:
    def __init__(self):
        self.param1 = None
        self.param2 = None
        self.param3 = None

    def set_param1(self, param1):
        self.param1 = param1
        return self

    def set_param2(self, param2):
        self.param2 = param2
        return self

    def set_param3(self, param3):
        self.param3 = param3
        return self

    def build(self):
        return Object(self.param1, self.param2, self.param3)


# Usage
builder = ObjectBuilder()
obj = builder.set_param1('value1').set_param3('value3').build()
