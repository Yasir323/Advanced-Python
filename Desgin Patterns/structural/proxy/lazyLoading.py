"""The Proxy pattern can be used for lazy loading of resources, especially when the resource loading is expensive or
time-consuming. The proxy delays the creation or loading of the resource until it is actually needed. This is useful
when dealing with large files, images, or database connections. """


class Resource:
    def __init__(self, name):
        self.name = name
        # Perform resource-intensive loading operation
        print(f"Loading resource: {self.name}")

    def use_resource(self):
        print(f"Using resource: {self.name}")


class ResourceProxy:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def use_resource(self):
        if self.resource is None:
            self.resource = Resource(self.name)
        self.resource.use_resource()


# Usage
proxy = ResourceProxy("large_file.txt")
proxy.use_resource()  # Loads the resource: large_file.txt
proxy.use_resource()  # Uses the already loaded resource: large_file.txt
