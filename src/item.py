import csv
import os


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

        Item.all.append(self)

    @property
    def name(self) -> str:
        '''
        геттер метод для получения приватного атрибута __name
        '''
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        '''
        сеттер метод для перезаписи атрибута __name
        '''
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    @classmethod
    def instantiate_from_csv(cls, path=os.path.join("..", "src", "items.csv")):
        '''
        открывает файт csv и на основе его данных создает экземпляры класса, которые записывает в список all
        '''
        cls.all.clear()
        if os.path.exists(path):
            with open(path, 'r', encoding='Windows-1251') as file:
                file_data = csv.DictReader(file)
                for row in file_data:
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    cls(name, price, quantity)

    @staticmethod
    def string_to_number(value):
        '''
        получает строку в которой записано число возвращает целое число округленное int
        '''
        return (int(float(value)))
