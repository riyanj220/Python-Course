class Animal:
    def speak(self):
        print("animal speaks")


class dog(Animal):
    def speak(self):
        print("dog barks")


dog1 = dog()
dog1.speak()


# ____________________________________________________________________
class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius * self.radius


rec = shape(3, 2)
print(rec.area())


c = circle(20)
print(c.area())
