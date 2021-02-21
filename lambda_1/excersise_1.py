from decimal import Decimal


def excersise_1():
    list_name = ["Damian", "Patryk", "Wojtek", "Jarek", "Lech"]
    print("Case A")

    result_a = sorted(list_name, key=lambda name: len(name))
    print(result_a)


class BankAccount():
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Account name {self.name} balance is {self.balance}"


def exercise_2_3():
    acc_1 = BankAccount("Acc1", Decimal(1000))
    acc_2 = BankAccount("Acc2", Decimal(2000))
    acc_3 = BankAccount("Acc3", Decimal(3000))
    acc_4 = BankAccount("Acc4", Decimal(4000))
    acc_5 = BankAccount("Acc5", Decimal(5000))

    account_list = [acc_1, acc_2, acc_3, acc_4, acc_5]

    print("Exercise 2")

    filter_account = list(filter(lambda acc: acc if acc.balance > Decimal(4500) else None, account_list))
    print(filter_account)

    print("Exercise 3")

    max_account = max(account_list, key=lambda  acc: acc.balance)