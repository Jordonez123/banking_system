import unittest

from banking_system.account import Account
class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account(account_number=123, balance=20)
    
    def test_deposit(self):
        self.assertEqual(self.account.deposit(30), 50)
    
    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(30), 20)

if __name__ == '__main__':
    unittest.main()