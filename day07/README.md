# Day 07 - Account Registry & Transaction History

## Overview

This project extends the Day 06 Banking System by introducing Data Structures and Algorithms (DSA).

The project uses:

- Dictionary (HashMap) for fast account lookup
- Stack (List) for transaction history
- Factory Design Pattern
- Observer Design Pattern
- Object-Oriented Programming (OOP)

---

## Project Structure

```text
day07/
│
├── accounts.py
├── observer.py
├── factory.py
├── registry.py
├── bank.py
└── README.md
```

---

## Features

### Account Management

- Create Savings Account
- Create Current Account
- Deposit money
- Withdraw money
- Add interest to Savings Account
- Print account statement

---

### Observer Pattern

Each transaction automatically sends notifications.

Observers:

- SMSAlert
- AuditLog

Example:

```
[SMS] Almaz deposited 500 ETB
[LOG] Almaz deposited 500 ETB
```

---

### Factory Pattern

Accounts are created using AccountFactory.

Example:

```python
acc = AccountFactory.create(
    "savings",
    "Almaz",
    "CBE-001",
    1500
)
```

---

### Account Registry (Dictionary)

All accounts are stored inside a dictionary.

Example:

```python
registry.add(account)

registry.find("CBE-001")
```

Time Complexity:

- Add → O(1)
- Find → O(1)

---

### Transaction History (Stack)

Every deposit and withdrawal is stored in a stack.

Example:

```
Deposit 500
Withdraw 200
Deposit 90
```

---

### Undo Last Transaction

Undo removes the latest transaction.

Example:

```
Before Undo

Deposit 500
Withdraw 200
Deposit 90

Undo

Deposit 90 removed
```

---

## Big-O Analysis

| Operation | Data Structure | Complexity |
|-----------|---------------|------------|
| Add Account | Dictionary | O(1) |
| Find Account | Dictionary | O(1) |
| Deposit | Stack | O(1) |
| Withdraw | Stack | O(1) |
| Undo Last Transaction | Stack | O(1) |
| List All Accounts | Sorting | O(n log n) |

---

## Technologies

- Python 3
- OOP
- Dictionary
- Stack
- Factory Pattern
- Observer Pattern

---

## How to Run

```bash
python bank.py
```

---

## Sample Output

```
[SMS] Almaz deposited 500 ETB
[LOG] Almaz deposited 500 ETB

[SMS] Almaz withdrew 200 ETB
[LOG] Almaz withdrew 200 ETB

Transaction History

Deposit : 90 ETB
Withdraw : 200 ETB
Deposit : 500 ETB

Undo Deposit : 90 ETB

Final Statement

Almaz | CBE-001 | Balance : 1800.00 ETB
```

---

## Learning Objectives

After completing this project I learned:

- Object-Oriented Programming
- Dictionary (HashMap)
- Stack
- Big-O Notation
- Factory Design Pattern
- Observer Design Pattern
- Transaction History
- Undo Operation

---

## Author

**Dawa**

Software Development Student

Day 07 - DSA I (Linear Structures & Big-O)