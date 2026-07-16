class Account:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.deposit(initial_balance)

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.__balance:
            raise ValueError("Insufficient funds for this withdrawal")
        self.__balance -= amount

