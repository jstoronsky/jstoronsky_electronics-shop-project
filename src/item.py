import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.error_message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.error_message


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
        super().__init__()
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
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        path = os.path.join(os.path.dirname(__file__), file_csv)
        if not os.path.exists(path):
            raise FileNotFoundError("Отсутствует файл items.csv")
        with open(path, "rt", encoding="windows-1251") as file:
            new_file = csv.DictReader(file)
            if len(new_file.fieldnames) < 3:
                raise InstantiateCSVError
            else:
                for position in new_file:
                    name = position['name']
                    price = position['price']
                    quantity = position['quantity']
                    cls.all.append(cls(name, price, quantity))

    @staticmethod
    def string_to_number(str_num):
        """
        статический метод, возвращающий число из числа-строки
        """
        int_num = int(float(str_num))
        return int_num

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        elif isinstance(self, other.__class__):
            return self.quantity + other.quantity
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name
