from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        используем функцию super для доступа к атрибутам родительского класса
        :param number_of_sim: количество сим-карт
        """
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError(f"Количество физических SIM-карт должно быть целым числом больше нуля")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sims):
        """
        Устанавливаем сеттер для количества сим-карт и прописываем условие, чтоб количество не могло быть нулём
        """
        if sims > 0:
            self.__number_of_sim = sims
        else:
            raise ValueError(f"Количество физических SIM-карт должно быть целым числом больше нуля")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
