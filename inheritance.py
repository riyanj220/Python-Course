# class employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showdetails(self):
#         print(f"the name of employee : {self.id} is {self.name}")


# e = employee("riyan", 400)
# e.showdetails()
# e1 = employee("ok", 232)
# e1.showdetails()


# class programmer(employee):
#     def showlanguage(self):
#         print("the default language is python")


# e3 = programmer("ali", 123)
# e3.showdetails()
# e3.showlanguage()


# _______________________________________________________________________________
class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"the name of employee : {self.id} is {self.name}")


class manager(employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def showdetails(self):
        print(
            f"the name of employee : {self.id} is {self.name} is in department of {self.department}"
        )


parent_class = employee("riyan", 400)
parent_class.showdetails()


child_class = manager("rio biscuit", 110, "software")
child_class.showdetails()
