from account import Account


def main():
    acc1 = Account("Addis", "1001", 500)
    acc2 = Account("Bank", "2002", 250)

    acc1.deposit(100)
    acc2.deposit(50)

    acc1.withdraw(200)
    acc2.withdraw(100)

    print("--- Balances after transactions ---")
    print(f"{acc1.owner} ({acc1.account_number}) balance: {acc1.balance}")
    print(f"{acc2.owner} ({acc2.account_number}) balance: {acc2.balance}")

    print("--- Rejected operations ---")
    try:
        acc1.deposit(-10)
    except ValueError as e:
        print(f"Deposit rejected: {e}")

    try:
        acc2.withdraw(1000)
    except ValueError as e:
        print(f"Withdrawal rejected: {e}")


if __name__ == "__main__":
    main()

