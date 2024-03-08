# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def speak(self):
#         print("sound made by animal")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="dog")
#         self.breed = breed

#     def speak(self):
#         print("bark")


# d = Dog("tom", "german")
# print(d.speak())


# d1 = Animal("daada", "dfadfaf")
# print(d1.speak())
# _____________________________________________________________________
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("sound made by animal")


class cat(Animal):
    def __init__(self, name, species, gender):
        Animal.__init__(self, name, species)
        self.gender = gender

    def speak(self):
        print("Meow")


a = Animal("lion", "predator")
a.speak()

b = cat("tom", "pet animal", "male")
a.speak()
