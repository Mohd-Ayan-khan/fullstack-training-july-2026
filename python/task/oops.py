class ATM:

    def __init__(self, bank_id, pin, amount, time):
        self._bank_id = bank_id
        self.__pin = pin
        self._amount = amount
        self.time = time

    def display(self):
        print(self._bank_id)
        print(self.__pin)
        print(self.__amount)
        print(self.time)


obj = ATM("112", 7000, 101, "1:00")

obj.display()
