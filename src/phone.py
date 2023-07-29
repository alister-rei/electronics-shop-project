from src.item import Item


class Phone(Item):
    '''
    Класс для телефонов в магазине
    '''

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        '''
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим карт в телефоне.
        '''
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        '''
        геттер метод для получения приватного атрибута __number_of_sim
        '''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        '''
        сеттер метод для перезаписи атрибута __number_of_sim
        '''
        if number_of_sim >= 1 and type(number_of_sim) == int:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self) -> str:
        '''
        Данные экземпляра класса для разработчика
        '''
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
