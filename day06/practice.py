class BankConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
         # shared configuration
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
# Create objects
a = BankConfig()
b = BankConfig()

# Check Singleton
print(a is b)

# Access same data
print(a.interest_rate)
print(b.interest_rate)
print(a.overdraft_limit)
print(b.overdraft_limit)