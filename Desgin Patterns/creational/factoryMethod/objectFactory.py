class MediaPlayer:
    def play(self):
        raise NotImplementedError()


class AudioPlayer(MediaPlayer):
    def play(self):
        print("Playing audio...")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("Playing video...")


class MediaPlayerFactory:
    def create_player(self, media_type):
        if media_type == 'audio':
            return AudioPlayer()
        elif media_type == 'video':
            return VideoPlayer()
        else:
            raise ValueError("Invalid media type")


# Usage
factory = MediaPlayerFactory()
audio_player = factory.create_player('audio')
audio_player.play()

video_player = factory.create_player('video')
video_player.play()
