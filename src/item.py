import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        overall_price_ = self.price * self.quantity
        return overall_price_

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        with open("/home/jstoronsky/hw_13.1-1/src/items.csv", "rt", encoding="windows-1251") as file:
            new_file = csv.DictReader(file)
            for position in new_file:
                name = position['name']
                price = position['price']
                quantity = position['quantity']
                cls.all.append(cls(name, price, quantity))

    @staticmethod
    def string_to_number(str_num):
        int_num = int(float(str_num))
        return round(int_num)
