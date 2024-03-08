# __len__(self): Defines the behavior of the len() function when called on objects of the class.
class Myclass:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)


mylist = Myclass(
    [
        1,
        2,
        3,
        4,
        5,
        56,
        6,
    ]
)
print(len(mylist))

# _____________________________________________________

# __str__ dunder =>
# Defines the string representation of an object when using the str() function or print().


# class Myclass:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"my class instance with value {self.value}"


# obj = Myclass(232)
# print(str(obj))

# __________________________________________________________

# __add__(self, other): Specifies how instances of a class should behave when using the + operator


# class Myclass:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Myclass(self.value + other.value)


# obj1 = Myclass(12)
# obj2 = Myclass(1212)
# result = obj1 + obj2

# print(result.value)

# ____________________________________________________________________________
