import csv
import os


class Item:
    '''
    Класс для представления товара в магазине.
    '''
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        '''
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        '''
        self.name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self) -> str:
        '''
        Данные экземпляра класса для разработчика
        '''
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        '''
        Данные по экземпляру класса для пользователя
        '''
        return f"{self.name}"

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

    @property
    def price(self) -> float:
        '''
        геттер метод для получения приватного атрибута __price
        '''
        return self.__price

    @property
    def quantity(self) -> int:
        '''
        геттер метод для получения приватного атрибута __quantity
        '''
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        '''
        сеттер метод для перезаписи атрибута __quantity
        '''
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Количество физических товаров должно быть целым числом от нуля.')
        self.__quantity = quantity

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
        self.__price = self.pay_rate * self.price

    def __add__(self, other) -> ValueError | int:
        '''
        Складывает объекты класса "Item" и дочерние от него
        '''
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты "Item" и дочерние от них.')
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, path=os.path.join(os.path.dirname(__file__), "..", "src", "items.csv")) -> None:
        '''
        открывает файт csv и на основе его данных создает экземпляры класса, которые записывает в список all
        '''
        cls.all.clear()
        if os.path.exists(path):
            with open(path, 'r', encoding='Windows-1251') as file:
                file_data = csv.DictReader(file)
                for row in file_data:
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)

    @staticmethod
    def string_to_number(value) -> int:
        '''
        получает строку в которой записано число возвращает целое число округленное int
        '''
        return int(float(value))
