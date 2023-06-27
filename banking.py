

class Client:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.balance = 0

    def get_balance(self):
        print(f"Баланс клиента: {self.balance}")

    def deposit(self, sum: int):
        self.balance += sum
        print(f"Баланс клиента {self.name} {self.surname} успешно пополнен на сумму {sum}\nТекущий баланс: {self.balance}")
    
    def withdraw(self, sum: int):
        if self.balance >= sum:
            self.balance -= sum
            print(f"Вывод средств успешно произведен.\nТекущий баланс: {self.balance}")
        else:
            print(f"Недостаточно средств.\nТекущий баланс: {self.balance}")


class Bank:

    def __init__(self, bankname: str):
        self.bankname = bankname

    def transaction(self, from_client, to_client, sum: int):
        if from_client.balance >= sum:
            from_client.balance -= sum
            to_client.balance += sum
            print('Перевод проведет успешно!')
        else:
            print('Недостаточно средств.')
MyBank = Bank('Mybank')
user1 = Client('Илья', 'Власов')
user2 = Client('Виктор', 'Баринов')
user1.deposit(500)
user2.deposit(250)
MyBank.transaction(user1, user2, 100)
user1.get_balance()
user2.get_balance()

