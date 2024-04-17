from  account import Account
from collections import defaultdict
from exceptions import CustomError
class Bank:
    def __init__(self) -> None:
        self.accounts_dictionary = defaultdict(int)
    
    def create_account(self, account_number: int) -> int:
        try:
            self.attempt_create_existing_account(account_number)
        except CustomError as e:
            print("Caught a custom error")
        else:
            new_account = Account(account_number)
            return new_account.account_number
       
    
    def attempt_create_existing_account(self, account_number: int):
        if account_number in self.accounts_dictionary.keys:
            raise CustomError("This account already exists")

    def check_existing_account(self, account_number: int):
        if account_number not in self.accounts_dictionary.keys:
            raise CustomError("This account does not exist")
    
    def get_account(self, account_number:int) -> Account:
        # neeed to check if account exists possible error
        try:
            self.check_existing_account(account_number)
        except CustomError as e:
            print("Caught a custom error", e)
        else:
            return self.accounts_dictionary[account_number]
    
    def close_account(self, account_number: int) -> None:
        # neeed to check if account exists possible error       
        try:
            self.check_existing_account(account_number)
        except CustomError as e:
            print("Caught a custom error", e)
        else:
            del self.accounts_dictionary[account_number]
        