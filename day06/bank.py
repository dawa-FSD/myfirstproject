from factory import AccountFactory
from observer import SMSAlert, AuditLog
from accounts import SavingsAccount
acc1 = AccountFactory.create(
    "savings",
    "Almaz",
    "CBE-001",
    1500
)
acc2 = AccountFactory.create(
    "current",
    "Dawit",
    "CBE-002",
    800
)
sms = SMSAlert()
log = AuditLog()
acc1.subscribe(sms)
acc1.subscribe(log)
acc2.subscribe(sms)
acc2.subscribe(log)
acc1.deposit(500)
acc1.withdraw(200)
if isinstance(acc1, SavingsAccount):
    acc1.add_interest()
acc2.deposit(300)
acc2.withdraw(100)
print("\nFinal Account Statements")
acc1.statement()
acc2.statement()