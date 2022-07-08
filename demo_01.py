# 小明爱跑步
class Person:
    def __init__(self, person_name, person_weight):
        self.name = person_name
        self.weight = person_weight

    def run(self):
        self.weight -= 0.5
        print("本次跑步会减肥0.5KG")

    def eat(self):
        self.weight += 1
        print("吃东西增长1KG体重")

    def __str__(self):
        return "%s 现在 %.1f KG" % (self.name, self.weight)


xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
print("_" * 50)
xiaomei = Person("小美", 45)
# xiaomei.run()
# xiaomei.eat()
print(xiaomei)