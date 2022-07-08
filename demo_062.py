class Aniaml:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")

    def run(self):
        print("跑")


class Dog(Aniaml):
    def bark(self):
        print("哇哇叫")


class Xiaotianquan(Dog):  # 这叫class
    def fly(self):
        print("我会飞")

    def bark(self):
        print("哈哈叫")
        # super().bark()
        print("dsadsa")
        Dog.bark(self)
        Xiaotianquan.bark(self)


xtq = Xiaotianquan()
xtq.bark()  # 如果子类中重写了父类的方法，在使用子类对象调用方法时，会调用子类中重写的方法
Xiaotianquan().fly()