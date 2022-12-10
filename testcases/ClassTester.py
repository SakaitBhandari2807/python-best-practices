import unittest
from classes.Account import Account


class AccountTest(unittest.TestCase):


    def test_withdraw(self):
        account = Account('Sakait', 100)
        account.withdraw(40)

        self.assertEqual(account.getcurrentbalance(), 60)

    def test_deposit(self):
        account = Account('Sao', 100)
        account.deposit(100)
        self.assertEqual(account.getcurrentbalance(), 200)


if __name__ == '__main__':
    unittest.main()