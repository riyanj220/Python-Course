# class parent:
#     def parent_method(self):
#         print("this is parent method")


# class child(parent):  # inherit krrha parent class ko
#     def parent_method(self):
#         print("riyan")
#         super().parent_method  # although parent class ka method ka naam hy yeh like q ke child class ne apna bana lia hy so instead ke wo parent class ko call krega wo child class ko hi call krega

#     def child_method(self):
#         print("this is child method")

#         super().parent_method()  # inherit krrha parent class ke parent method ko


# child_object = child()
# child_object.child_method()

# child_object.parent_method()

# _____________________________________________________________________________


class Employee:
    def __init__(self, naem, id):
        self.name = naem
        self.id = id


class programmer(Employee):
    def __init__(self, name, id, lan):
        super().__init__(name, id)
        self.lan = lan
