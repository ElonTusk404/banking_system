class Bank:
    clients_count = 0

    def __init__(self, name):
        self.bankname = name
        self.clients = {}

    def create_client(self, name, balance):
        return Client(name, balance)

    def transaction(self, from_client, to_client, amount):
        if from_client.get_balance() >= amount:
            from_client.withdraw(amount)
            to_client.deposit(amount)
            print('Перевод проведен успешно!')
        else:
            print('Недостаточно средств.')


class Client:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Баланс клиента {self._name} успешно пополнен на сумму {amount}\nТекущий баланс: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Вывод средств успешно произведен.\nТекущий баланс: {self._balance}")
        else:
            print(f"Недостаточно средств.\nТекущий баланс: {self._balance}")

    def get_balance(self):
        return self._balance
