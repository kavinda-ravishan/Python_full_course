class A:
    def __init__(self):
        print("A init")

    def Feature1(self):
        print("Feature 1 : working")

    def Feature2(self):
        print("Feature 2 : working")

    def Common(self):
        print("Common A: working")


class B:
    def __init__(self):
        print("B init")

    def Feature3(self):
        print("Feature 3 : working")

    def Feature4(self):
        print("Feature 4 : working")

    def Common(self):
        print("Common B: working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

    def Feature(self):
        super().Feature1()


c = C()
c.Feature1()
c.Feature2()
c.Feature3()
c.Feature4()
c.Common()
c.Feature()
