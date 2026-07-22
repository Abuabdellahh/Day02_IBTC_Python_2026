from __future__ import annotations

from bank import Account, AccountFactory, SMSAlert


class AccountRegistry:
    """Stores accounts keyed by number for O(1) add and lookup.

    A dict gives average-case O(1) `add` and `find` (hash of the number ->
    slot), versus O(n) if we scanned a list looking for a matching number.
    `list_all` is unavoidably O(n): it must touch every account.
    """

    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def add(self, account: Account) -> None:  # O(1)
        if account.account_number in self._accounts:
            raise ValueError(f"Account {account.account_number!r} is already registered")
        self._accounts[account.account_number] = account

    def find(self, account_number: str) -> Account:  # O(1)
        try:
            return self._accounts[account_number]
        except KeyError:
            raise KeyError(f"No account with number {account_number!r}") from None

    def list_all(self) -> list[Account]:  # O(n), in insertion order
        return list(self._accounts.values())

    def __len__(self) -> int:
        return len(self._accounts)

    def __contains__(self, account_number: str) -> bool:  # O(1)
        return account_number in self._accounts


if __name__ == "__main__":
    registry = AccountRegistry()
    registry.add(AccountFactory.create("savings", "Bob", "SAV-002", initial_balance=1000, rate=0.05))
    registry.add(AccountFactory.create("current", "Carol", "CUR-003", initial_balance=200, overdraft=300))

    # O(1) lookup by account number.
    bob = registry.find("SAV-002")
    bob.subscribe(SMSAlert(phone_number="+1-555-0100"))

    bob.deposit(500)
    bob.withdraw(200)
    print("History after deposit + withdraw:")
    for tx in bob.history:
        print(f"  {tx.kind:<10} ${tx.amount:.2f}")

    undone = bob.undo_last()
    print(f"\nUndid last: {undone.kind} of ${undone.amount:.2f}")
    print(f"Balance restored to: ${bob.balance:.2f}\n")

    print(f"Registry holds {len(registry)} accounts:")
    for acc in registry.list_all():
        print(f"  {acc.statement()}")
