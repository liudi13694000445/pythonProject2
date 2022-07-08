class A:
    def test(self):
        print("这个是A ---test")

    def demo(self):
        print("这是A  ---demo")


class B:
    def demo(self):
        print("这是B  ---demo")

    def test(self):
        print("这个是B ---test")


class C(B, A):
    pass


c = C()
c.test()
c.demo()
print(C.__mro__)