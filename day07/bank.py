from __future__ import annotations

from abc import ABC, abstractmethod
from typing import NamedTuple


class Transaction(NamedTuple):
    kind: str  # "deposit" or "withdrawal"
    amount: float


class Account:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0) -> None:
        self.owner = owner
        self.account_number = account_number
        self.__balance: float = 0
        self._alerts = AlertService()
        self._history: list[Transaction] = []
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        if initial_balance:
            self.deposit(initial_balance)

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def history(self) -> tuple[Transaction, ...]:
        return tuple(self._history)

    def subscribe(self, observer: AccountObserver) -> None:
        self._alerts.subscribe(observer)

    def unsubscribe(self, observer: AccountObserver) -> None:
        self._alerts.unsubscribe(observer)

    def _notify(self, event: str, amount: float) -> None:
        self._alerts.notify(event, self, amount)

    def _available(self) -> float:
        """Funds that may be withdrawn; subclasses widen this (e.g. overdraft)."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.__balance += amount
        self._history.append(Transaction("deposit", amount))
        self._notify("deposit", amount)

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self._available():
            raise ValueError("Insufficient funds for this withdrawal")
        self.__balance -= amount
        self._history.append(Transaction("withdrawal", amount))
        self._notify("withdrawal", amount)

    def undo_last(self) -> Transaction:
        """Pop the most recent transaction (LIFO) and reverse its effect on the balance."""
        if not self._history:
            raise ValueError("No transactions to undo")
        last = self._history.pop()
        if last.kind == "deposit":
            self.__balance -= last.amount
        else:
            self.__balance += last.amount
        return last

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

    def _available(self) -> float:
        return self.balance + self.overdraft

    def statement(self) -> str:
        return f"Current Account | {self.owner} ({self.account_number}) | Balance: ${self.balance:.2f} | Overdraft: ${self.overdraft:.2f}"


class AccountObserver(ABC):
    """Interface every account alert channel must implement (SOLID: DIP + ISP)."""

    @abstractmethod
    def notify(self, event: str, account: Account, amount: float) -> None:
        ...


class SMSAlert(AccountObserver):
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def notify(self, event: str, account: Account, amount: float) -> None:
        print(
            f"[SMS to {self.phone_number}] {account.owner}: {event} of ${amount:.2f} "
            f"on {account.account_number}. New balance: ${account.balance:.2f}"
        )


class AlertService:
    """Owns the observer list and dispatches events; Account no longer does this itself (SRP)."""

    def __init__(self) -> None:
        self._observers: list[AccountObserver] = []

    def subscribe(self, observer: AccountObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: AccountObserver) -> None:
        self._observers.remove(observer)

    def notify(self, event: str, account: Account, amount: float) -> None:
        for observer in self._observers:
            observer.notify(event, account, amount)


class AccountFactory:
    _registry: dict[str, type[Account]] = {
        "savings": SavingsAccount,
        "current": CurrentAccount,
    }

    @classmethod
    def create(cls, kind: str, owner: str, account_number: str, **kwargs) -> Account:
        try:
            account_cls = cls._registry[kind.lower()]
        except KeyError:
            raise ValueError(f"Unknown account kind: {kind!r}") from None
        return account_cls(owner, account_number, **kwargs)


if __name__ == "__main__":
    accounts: list[Account] = [
        AccountFactory.create("savings", "Bob", "SAV-002", initial_balance=1000, rate=0.05),
        AccountFactory.create("current", "Carol", "CUR-003", initial_balance=200, overdraft=300),
    ]

    for acc in accounts:
        acc.subscribe(SMSAlert(phone_number="+1-555-0100"))

    accounts[0].add_interest()
    accounts[1].withdraw(400)

    for acc in accounts:
        print(acc.statement())
