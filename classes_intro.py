# class gym:
#     name = "riyan"
#     age = 18
#     fees = "paid"

#     def progress(self):
#         print(f"{self.name} having age {self.age}, have {self.fees} their fees")


# person = gym()
# person.name = "Ali"
# person.age = 17
# person.fees = "not paid"
# person.progress()


class robot:
    def __init__(
        self, name, color
    ):  # constructor ,agar ham chahty hy ke ke certain class ke kisi object ko banane ke bad kuch lazmi execute ho to bana skty isko
        self.name = name
        self.color = color

    def introduction(self):
        print(f"i am {self.name} and my color is {self.color}")


robot1 = robot("robo1", "red")
robot2 = robot("robo2", "green")

robot1.introduction()
robot2.introduction()
