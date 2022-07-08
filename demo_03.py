class MusicPlayer(object):

    instance = None

    init_flag = False

    def __new__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):

        if MusicPlayer.init_flag:
            return

        print("播放音乐器")

        MusicPlayer.init_flag = True



play1 = MusicPlayer()
print(play1)

play2 = MusicPlayer()
print(play2)