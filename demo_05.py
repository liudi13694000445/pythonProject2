class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))


xiaomei = Women("小美")
# xiaomei.secret()
print(xiaomei._Women__age)
xiaomei._Women__secret()