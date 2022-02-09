class A:
    def Feature1(self):
        print("Feature 1 : working")

    def Feature2(self):
        print("Feature 2 : working")


class B(A):
    def Feature3(self):
        print("Feature 3 : working")

    def Feature4(self):
        print("Feature 4 : working")


class C:
    def Feature5(self):
        print("Feature 5 : working")


class D(B, C):
    pass


def main():
    b = B()
    b.Feature1()
    b.Feature2()
    b.Feature3()
    b.Feature4()

    d = D()
    d.Feature5()


if __name__ == "__main__":
    main()
