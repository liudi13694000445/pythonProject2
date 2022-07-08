class Dog:

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫的和神一样")
        Dog().bark()
        super(XiaoTianQuan, self).bark()


xtq = XiaoTianQuan()
xtq.bark()