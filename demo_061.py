class MusicPlayer(object):

    instance = None

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance
6
    def __init__(self):

        print("播放音乐器")


play1 = MusicPlayer()
print(play1)

play2 = MusicPlayer()
print(play2)