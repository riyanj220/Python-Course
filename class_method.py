class Employee:
    company = "apple"

    def show(self):
        print(f"the name is {self.name} and the company's name is {self.company}")

    @classmethod  # class ke variable ko change kardega yeh
    def change_company(self, new_company):
        self.company = new_company


e1 = Employee()
e1.name = "riyan"
e1.show()
e1.change_company("tesla")
e1.show()

print(Employee.company)
# for example agr me yeh na lagao aur class variable print krun hala ke mene ik def use kr ke isko change krdiya hy iske bawajood ye class variavle change ni krega but agr me class method ka decorator laga du to ye class variable change krdega
