class Employee:
    company_name = "apple"  # class variables

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02  # instance variables

    def showdetails(self):
        print(
            f"the name of employee is {self.name} and the raise amount is {self.raise_amount} in {self.company_name}"
        )


e = Employee("riyan")
e.raise_amount = 0.5
e.company_name = "pak fans"
e.showdetails()


e2 = Employee("rio")
e2.showdetails()
