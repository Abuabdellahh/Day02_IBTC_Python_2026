class Account:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0) -> None:
        self.owner = owner
        self.account_number = account_number
        self.__balance: float = 0
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

    def statement(self) -> str:
        return f"Account | {self.owner} ({self.account_number}) | Balance: ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0, rate: float = 0.0) -> None:
        super().__init__(owner, account_number, initial_balance)
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self.rate = rate

    def add_interest(self) -> None:
        self.deposit(self.balance * self.rate)

    def statement(self) -> str:
        return f"Savings Account | {self.owner} ({self.account_number}) | Balance: ${self.balance:.2f} | Rate: {self.rate:.1%}"


class CurrentAccount(Account):
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0, overdraft: float = 0) -> None:
        super().__init__(owner, account_number, initial_balance)
        if overdraft < 0:
            raise ValueError("Overdraft limit cannot be negative")
        self.overdraft = overdraft
        self._overdraft_used: float = 0

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        available = self.balance + (self.overdraft - self._overdraft_used)
        if amount > available:
            raise ValueError("Exceeds overdraft limit")
        shortfall = max(0.0, amount - self.balance)
        if shortfall > 0:
            self._overdraft_used += shortfall
            self.deposit(shortfall)  # bring balance to zero so parent withdraw succeeds
        super().withdraw(amount)

    def statement(self) -> str:
        return f"Current Account | {self.owner} ({self.account_number}) | Balance: ${self.balance:.2f} | Overdraft: ${self.overdraft:.2f}"


if __name__ == "__main__":
    accounts: list[Account] = [
        Account("Alice", "ACC-001", 500),
        SavingsAccount("Bob", "SAV-002", 1000, rate=0.05),
        CurrentAccount("Carol", "CUR-003", 200, overdraft=300),
    ]

    # Add interest to savings accounts before printing
    for acc in accounts:
        if isinstance(acc, SavingsAccount):
            acc.add_interest()

    for acc in accounts:
        print(acc.statement())
