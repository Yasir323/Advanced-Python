# The interface of a remote service.
class ThirdPartyYouTubeLib:
    def listVideos(self):
        # Send an API request to YouTube.
        raise NotImplementedError

    def getVideoInfo(self, id):
        # Get metadata about some video.
        raise NotImplementedError

    def downloadVideo(self, id):
        # Download a video file from YouTube.
        raise NotImplementedError


# The concrete implementation of a service connector. Methods
# of this class can request information from YouTube. The speed
# of the request depends on a user's internet connection as
# well as YouTube's. The application will slow down if a lot of
# requests are fired at the same time, even if they all request
# the same information.
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def listVideos(self):
        # Send an API request to YouTube.
        pass

    def getVideoInfo(self, id):
        # Get metadata about some video.
        pass

    def downloadVideo(self, id):
        # Download a video file from YouTube.
        pass


# To save some bandwidth, we can cache request results and keep
# them for some time. But it may be impossible to put such code
# directly into the service class. For example, it could have
# been provided as part of a third party library and/or defined
# as `final`. That's why we put the caching code into a new
# proxy class which implements the same interface as the
# service class. It delegates to the service object only when
# the real requests have to be sent.
class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service):
        self.__service = service
        self.__listCache = None
        self.__videoCache = None
        self.needReset = False

    def listVideos(self):
        if self.__listCache is None or self.needReset:
            self.__listCache = self.__service.listVideos()
        return self.__listCache

    def getVideoInfo(self, id):
        if self.__videoCache is None or self.needReset:
            self.__videoCache = self.__service.getVideoInfo(id)
        return self.__videoCache

    def downloadVideo(self, id):
        if not self.downloadExists(id) or self.needReset:
            self.__service.downloadVideo(id)

    def downloadExists(self, id):
        # Check if the video download exists.
        pass


# The GUI class, which used to work directly with a service
# object, stays unchanged as long as it works with the service
# object through an interface. We can safely pass a proxy
# object instead of a real service object since they both
# implement the same interface.
class YouTubeManager:
    def __init__(self, service):
        self._service = service

    def renderVideoPage(self, id):
        info = self._service.getVideoInfo(id)
        # Render the video page.

    def renderListPanel(self):
        videoList = self._service.listVideos()
        # Render the list of video thumbnails.

    def reactOnUserInput(self):
        self.renderVideoPage()
        self.renderListPanel()


# The application can configure proxies on the fly.
class Application:
    def init(self):
        aYouTubeService = ThirdPartyYouTubeClass()
        aYouTubeProxy = CachedYouTubeClass(aYouTubeService)
        manager = YouTubeManager(aYouTubeProxy)
        manager.reactOnUserInput()
