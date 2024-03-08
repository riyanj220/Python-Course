# class Baseclass:
#     def xyz(self):
#         print("this is base class")


# class derivedclass(Baseclass):
#     def xyz(self):
#         print("this is derived class")


# class derivedclass1(derivedclass):
#     def xyz(self):
#         print("this is derived class from the derived class")


# a = Baseclass()
# b = derivedclass()
# c = derivedclass1()


# a.xyz()
# b.xyz()
# c.xyz()


# _______________________________________________________________________
"""
multi level inheritance ka matlb generation smjhow pehly abbu phir beta phir 
uska beta
ab for example is program me ham ne teen class banayi jo level by level ik
dosre se link thi
ab ham agar golden class ka show details call karen ge to wo dog class ke show 
details me jayega phir whn se animal class ke show details me jayega
"""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name : {self.name} ")
        print(f"Specie : {self.species} ")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


class Goldenretreiver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden retreiver")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"color : {self.color}")


a = Animal("tom", "black")
a.show_details()
