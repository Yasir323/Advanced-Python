class LazyObject:
    def __init__(self):
        self._initialized = False
        self._value = None

    @property
    def value(self):
        if not self._initialized:
            self._initialize()
            self._initialized = True
        return self._value

    def _initialize(self):
        # Perform expensive initialization or loading
        # operations here and assign the result to self._value
        self._value = "Lazy loaded value"


# Usage
lazy_obj = LazyObject()

# The object is not initialized yet
print(lazy_obj.value)  # Lazy loaded value

# The object is already initialized, so the value is retrieved directly
print(lazy_obj.value)  # Lazy loaded value
