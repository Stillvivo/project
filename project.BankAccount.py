class bankAccount:
    def __init__(self, name, family, balance=0):
        self.name = name
        self.balance = balance
        self.family = family

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("you can't deposit zero")

    def withdraw(self, amount):
        if amount <= 0:
            print("you can't withdraw zero")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.name} your balance is: {self.balance}")


def main():
    print("welcome to bank account")

    name = input("please enter your name:")
    family = input("please enter your family:")
    account = bankAccount(name, family)
    print(f"({name}{family}) welcome to bank account")

    while True:
        print("------menu------")
        print("1.show balance account")
        print("2.deposit account")
        print("3.withdraw account")
        print("4. exit")

        choice = input("please enter your choice:")
        if choice == "1":
            account.show_balance()
        elif choice == "2":
            try:
                amount = float(input("please enter your amount:"))
                account.deposit(amount)
            except ValueError:
                print("please enter a valid number")
        elif choice == "3":
            try:
                amount = float(input("please enter your amount:"))
                account.withdraw(amount)
            except ValueError:
                print("please enter a valid number")
        elif choice == "4":
            print("GoodBye")
            break
        else:
            print("please choice a correct choice")


if __name__ == "__main__":
    main()
