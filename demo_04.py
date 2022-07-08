class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s]没有子弹了" % self.model)
            return
        else:
            self.bullet_count -= 1
            print("[%s]发射一颗子弹，剩余[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):

        if self.gun is None:
            print("[%s]快去领取一把枪" % self.name)

            return

        print("冲啊")
        self.gun.add_bullet(10)
        self.gun.shoot()


ak47 = Gun("AK47")
# ak47.add_bullet(10)
# ak47.shoot()

xusanduo = Soldier("许三多")

xusanduo.fire()
