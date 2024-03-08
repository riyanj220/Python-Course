# class employee:
#     def __init__(self, name, salaray):
#         self.name = name
#         self.salary = salaray

#     @classmethod
#     def fromstr(self, string):
#         return self(string.split("-")[0], int(string.split("-")[1]))


# e = employee("riyan", 12000)
# print(e.name)
# print(e.salary)


# string = "riyan-12000"
# e1 = employee.fromstr(string)
# print(e1.name)
# print(e1.salary)

# __________________________________________________________________________
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(self, string):
#         name, age = string.split(",")
#         return self(name, int(age))


# person1 = person.from_string("asda,20")
# print(person1.name, person1.age)
