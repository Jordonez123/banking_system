from src.src.banking_system.exceptions import CustomError

class Account:
    def __init__(self, account_number: int, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int) -> None:
        # need to check that deposit is > 0!
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
    