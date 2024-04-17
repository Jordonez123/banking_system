from src.banking_system.banking_system.exceptions import CustomError

class Account:
    def __init__(self, account_number: int, balance: int):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount
        return
    
    def check_overdraft(self):
        if self.balance == 0:
            raise CustomError("You are about to perform an overdraft")
        
    def withdraw(self, amount: int) -> None:
        try:
            self.check_overdraft()
        except CustomError as e:
            print("Caught a custom error:", e)
        else:
            self.balance -= amount
        
        return

    def get_balance(self) -> int:
        return self.balance
    