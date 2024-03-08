# public access specifiers

# ____________________________________________________________
# class myclass:
#     def __init__(self):
#         self.public_variable = "im public variable"

#     def public_method(self):
#         return "i am public method"


# obj = myclass()
# print(obj.public_variable)
# print(obj.public_method())

# __________________________________________________________________________
# private access specifiers
# _________________________________________________________________________


# class employee:
#     def __init__(self):
#         self.__name = "riyan"


# a = employee()
# # print(a.__name) #it cant be accessed directly as it will throw error q ke ye private h
# print(a._employee__name) #ab ese private ko b access kr skty hy aap


# ____________________________________________________________________________
# class myclass:
#     def __init__(self):
#         self.__public_variable = "im public variable" #=>>> ese private bana skty attribute ko

#     def __public_method(self):  #=>>>>ese private bana skty method ko
#         return "i am public method"


# obj = myclass()
# print(obj.__public_variable)     #=>>>cant access private attributes
# print(obj.__public_method())

# print(obj._myclass__public_method()) # =>>>  ese access krskty private ko


# ________________________________________________________________________________


# protected access specifiers


# class Car:
#     def __init__(self, price, color):
#         self._price = price
#         self.color = color

#     def _profit(self):
#         self.profit = 20_000


# c1 = Car(300000, "red")
# c2 = Car(450_000, "blue")


# print(c1._price) # This will work, but it's not recommended
