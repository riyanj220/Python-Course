# getters example (ese ham class ko chere bagher uske chzene nikaal skty hy)

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age


# student1 = student("riyan", 19)
# print(student1.get_name())
# print(student1.get_age())


# setters example


# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def set_name(self, new_name):
#         if isinstance(new_name, str):
#             self.name = new_name
#         else:
#             print("name must be a string")

#     def set_age(self, new_age):
#         if isinstance(new_age, int):
#             self.age = new_age
#         else:
#             print("age must be a non negative integer")


# student1 = student("riyan", 18)

# student1.set_name("rio biscuit")
# student1.set_age(200)

# print(student1.name)
# print(student1.age)

# _____________________________________________________________
# class myclass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"value is {self._value} ")

#     @property #a hidden way to make getter
#     def ten_value(self):
#         return 10 * self._value


# obj = myclass(10)
# print(obj.ten_value)
# obj.show()


# class myclass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"value is {self._value} ")

#     @property #a way to make getter
#     def ten_value(self):
#         return 10 * self._value

#     @ten_value.setter #a way to make setter {syntax = (property name .setter)}
#     def ten_value(self, new_value):
#         self._value = new_value / 10


# obj = myclass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()
