# class vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i +{self.j}j+ {self.k}k"

#     def __add__(self, x):
#         return vector(self.i + x.i, self.j + x.j, self.k + x.k)


# v1 = vector(3, 4, 6)
# print(v1)

# v2 = vector(5, 13, 13)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))


# ______________________________________________________________________________
class number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __add__(self, other):
        if isinstance(other, number):
            return number(self.x + other.x, self.y + other.y)

        else:
            raise TypeError("un supported operand type")


a = number(12121212121, 2)
print(a)
b = number(31211212313133, 4)
print(b)


"""
abhi for example agr me "a" object aur "b" object ko add krna chhau to ye nahi hoga
q ke a aur b ke drmiyan ko operator overloading ni hy
computer ko ni pta ye a aur b kia hy
hamko define krna prega
isiliye def __add__ use kia ta ke comp ko pta lage ke ye a aur b ko add krna hy

"""
print(a + b)
