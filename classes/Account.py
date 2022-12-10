class Account:
    bank_name = "ICICI"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("No sufficient account balance")
        else:
            print(f"debited {amount}")
            self.balance -= amount
            # return self.getcurrentbalance()

    def getcurrentbalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        # return self.getcurrentbalance()


# account1 = Account('Sakait', 100)
# print(account1.getcurrentbalance())
# print(account1.deposit(100))
# print(account1.withdraw(199))