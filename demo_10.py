class Musicplayer:

    def __new__(cls, *args, **kwargs):
        print("__new__")

        return super().__new__(cls)

    def __init__(self):
        print("__init__")


player = Musicplayer()
print(player)