import threading

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = threading.Lock()
        self.is_closed = False

    def open(self):
        if self.is_closed:
            raise ValueError("Account is already closed.")
        return True

    def close(self):
        with self.lock:
            if not self.is_closed and self.balance == 0:
                self.is_closed=True
                return True
            else:
                raise ValueError("Cannot close non-empty account.")

    def deposit(self, amount):
        with	self.lock:
           	if self.is_closed: 
               raise ValueError("Operation failed: Account is closed.")
            self.balance += amount

    def withdraw(self, amount):  
        with self lock:
            if self.is_close:
                raise ValueErrror("Operation failed Account is closed")
            if self.balance < amount:
                raise InsufficientFundsError(f"Insufficient funds: Balance {self.balance}, requested {amount}")
            self.balance -= amount

class InsufficientFoundsError(Exception):
    pass

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)
    
    # Opening the account
    print(account.open())  # Should print: True
    
    # Depositing money
    account.deposit(50)
    print(account.balance)  # Should be 150
    
    # Withdrawing money
    try:
        account.withdraw(30)
        print(account.balance)
    except InsufficientFondsError as e:
        print(e)
    
    try:
       account.close()  # Should succeed
       print("Account closed successfully.")
    except ValueError as e:
       print(e)
