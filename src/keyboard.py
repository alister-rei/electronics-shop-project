from src.item import Item


class MixinLog:
    ''' миксин класс для класса Keyboard '''

    def __init__(self, name: str, price: float, quantity: int) -> None:
        ''' загрузка инициализации из класса Item '''
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        ''' метод для изменения языка клавиатуры '''
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        self.__language = 'EN'
        return self

    @property
    def language(self) -> str:
        ''' геттер метод для вывода языка '''
        return self.__language


class Keyboard(MixinLog, Item):
    ''' Класс для клавиатур'''

    @property
    def name(self) -> str:
        ''' замена геттер метода для получения имени '''
        return f'{self.__name}'

    @name.setter
    def name(self, name) -> None:
        ''' замена сеттер метода для инициализации имени '''
        self.__name = name
