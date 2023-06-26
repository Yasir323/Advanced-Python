"""The Chain of Responsibility pattern can be used for implementing authorization and access control in an
application. Each handler in the chain can represent a different access control rule or permission level. The request
for accessing a resource can be passed through the chain, and each handler can decide whether to grant or deny access
based on the user's credentials or other criteria. This allows for fine-grained control over access permissions and
easy modification or extension of access control rules. """


class AccessControlHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def check_access(self, user, resource):
        pass


class PermissionCheckHandler(AccessControlHandler):
    def check_access(self, user, resource):
        if self.check_permission(user, resource):
            print("Access granted.")
        elif self.successor is not None:
            self.successor.check_access(user, resource)

    def check_permission(self, user, resource):
        # Perform permission check logic
        return True  # or False


class RoleCheckHandler(AccessControlHandler):
    def check_access(self, user, resource):
        if self.check_role(user, resource):
            print("Access granted.")
        elif self.successor is not None:
            self.successor.check_access(user, resource)

    def check_role(self, user, resource):
        # Perform role check logic
        return True  # or False


# Usage
user = None
resource = None
access_control = PermissionCheckHandler(RoleCheckHandler())
access_control.check_access(user, resource)
