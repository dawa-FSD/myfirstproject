from accounts import SavingsAccount, CurrentAccount


class AccountFactory:

    @staticmethod
    def create(account_type, owner, number, balance):
        if account_type.lower() == "savings":
            return SavingsAccount(owner, number, balance)
        elif account_type.lower() == "current":
            return CurrentAccount(owner, number, balance)
        else:
            raise ValueError("Invalid account type")