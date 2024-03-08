"""
subclass ke 2 parent hona multiple inheritance keh lata hy
"""


class Parent:
    def method1(self):
        print("method 1 from parent 1")


class Parent1:
    def method2(self):
        print("method 2 from parent 2")


class child(
    Parent1, Parent  # inheriting 2 parent class
):  # ab dekho ye class 2 parent class inherit krrhi ik saath thats  why it is called multiple inheritance
    def child_method(self):
        print("child method")


child1 = child()
child2 = child()
child1.method1()
child2.method2()

print(child.mro())
