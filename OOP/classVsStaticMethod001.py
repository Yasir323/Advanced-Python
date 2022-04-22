class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


print(MyClass.classmethod())
print(MyClass.staticmethod())
try:
    print(MyClass.method())
except TypeError as e:
    print(str(e))

print('-' * 50)

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
