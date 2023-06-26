# The collection interface must declare a factory method for
# producing iterators. You can declare several methods if there
# are different kinds of iteration available in your program.
class SocialNetwork:
    def createFriendsIterator(self, profileId):
        raise NotImplementedError

    def createCoworkersIterator(self, profileId):
        raise NotImplementedError


# Each concrete collection is coupled to a set of concrete
# iterator classes it returns. But the client isn't, since the
# signature of these methods returns iterator interfaces.
class Facebook(SocialNetwork):
    # ... The bulk of the collection's code should go here ...

    # Iterator creation code.
    def createFriendsIterator(self, profileId):
        return FacebookIterator(self, profileId, "friends")

    def createCoworkersIterator(self, profileId):
        return FacebookIterator(self, profileId, "coworkers")


# The common interface for all iterators.
class ProfileIterator:
    def getNext(self):
        pass

    def hasMore(self):
        pass


# The concrete iterator class.
class FacebookIterator(ProfileIterator):
    # The iterator needs a reference to the collection that it
    # traverses.
    def __init__(self, facebook, profileId, type):
        self.facebook = facebook
        self.profileId = profileId
        self.type = type

        # An iterator object traverses the collection independently
        # from other iterators. Therefore it has to store the
        # iteration state.
        self.currentPosition = 0
        self.cache = None

    def lazyInit(self):
        if self.cache is None:
            self.cache = self.facebook.socialGraphRequest(self.profileId, self.type)

    # Each concrete iterator class has its own implementation
    # of the common iterator interface.
    def getNext(self):
        if self.hasMore():
            self.currentPosition += 1
            return self.cache[self.currentPosition]

    def hasMore(self):
        self.lazyInit()
        return self.currentPosition < len(self.cache)


def sendEmail(email, message):
    pass


# Here is another useful trick: you can pass an iterator to a
# client class instead of giving it access to a whole
# collection. This way, you don't expose the collection to the
# client.
#
# And there's another benefit: you can change the way the
# client works with the collection at runtime by passing it a
# different iterator. This is possible because the client code
# isn't coupled to concrete iterator classes.
class SocialSpammer:
    def send(self, iterator, message):
        while iterator.hasMore():
            profile = iterator.getNext()
            sendEmail(profile.getEmail(), message)


# The application class configures collections and iterators
# and then passes them to the client code.
class Application:
    # def config(self):
    #     if working with Facebook:
    #         self.network = Facebook()
    #     if working with LinkedIn:
    #         self.network = LinkedIn()
    #     self.spammer = SocialSpammer()

    def sendSpamToFriends(self, profile):
        iterator = self.network.createFriendsIterator(profile.getId())
        self.spammer.send(iterator, "Very important message")

    def sendSpamToCoworkers(self, profile):
        iterator = self.network.createCoworkersIterator(profile.getId())
        self.spammer.send(iterator, "Very important message")
