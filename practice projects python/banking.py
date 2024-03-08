class Bank_account:
    banks_name = "Meezan Bank"

    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to your account . New balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Withdraw {amount} amount from your account .New balance : {self.balance}"
            )

        else:
            print("Insufficient Funds! withdrawal failed")

    def checks_balance(self):
        print(f"account balance for {self.name} is {self.balance}")


name = input("Enter Your name : ")
initial_balance = int(input("enter your initial balance: "))


# created instance/object of class bank account
myaccount = Bank_account(name, initial_balance)

while True:
    print("\nOptions: ")
    print("1. deposit")
    print("2. withdram")
    print("3. check balance")
    print("4. quit")

    choice = input("Choose options from above: ")

    if choice == "1":
        amount = int(input("eneter amount to deposit:"))
        myaccount.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount to Withdraw: "))
        myaccount.withdraw(amount)

    elif choice == "3":
        myaccount.checks_balance()

    elif choice == "4":
        print(f"Thank you for banking with {Bank_account.banks_name}")
        break

    else:
        print("invalid input! please enter a valid option")
