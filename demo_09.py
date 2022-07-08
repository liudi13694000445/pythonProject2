class Tools:
    count = 0

    @classmethod
    def show_tool(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tools.count += 1


tool1 = Tools("1")
Tools.show_tool()