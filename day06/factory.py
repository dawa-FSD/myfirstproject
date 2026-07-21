from accounts import SavingsAccount, CurrentAccount
class AccountFactory:
    @staticmethod
    def create(kind, owner, account_number, balance=0):
        if kind.lower() == "savings":
            return SavingsAccount(owner, account_number, balance)
        elif kind.lower() == "current":
            return CurrentAccount(owner, account_number, balance)
        raise ValueError("Unknown account type")