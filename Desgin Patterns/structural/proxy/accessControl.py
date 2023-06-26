"""Proxies can be used for implementing authorization and access control mechanisms. The proxy intercepts method
calls and checks whether the client has the necessary permissions before forwarding the request to the underlying
object. """


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}")
        else:
            print("Insufficient funds")


class BankAccountProxy:
    def __init__(self, account_number, balance, is_admin=False):
        self.account_number = account_number
        self.balance = balance
        self.is_admin = is_admin
        self.bank_account = BankAccount(account_number, balance)

    def withdraw(self, amount):
        if self.is_admin or self.balance >= amount:
            self.bank_account.withdraw(amount)
        else:
            print("Insufficient funds")


# Usage
proxy = BankAccountProxy("123456789", 1000)
proxy.withdraw(500)  # Withdrew 500 from account 123456789
proxy.withdraw(1000)  # Insufficient funds
