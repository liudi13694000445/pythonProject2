class Game:
    top_score = 0

    @classmethod
    def show_top_score(cls):
        print("历史最高分是 %d 分" % cls.top_score)

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print(" %s 开始游戏啦" % self.player_name)


# 查看帮助
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象，开始游戏
game = Game("小明")
game.start_game()
