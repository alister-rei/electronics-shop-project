import pytest

from src.item import Item, InstantiateCSVError
import os


# Тесты для проверки класса для ДЗ 13.1 homework_1
def test_item():
    item1 = Item("Смартфон", 10000, 10)

    # Тест атрибутов экземпляра класса
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 10

    # Тест методов класса
    assert item1.calculate_total_price() == 100000
    # Тест атрибута класса для метода
    item2 = Item("Samsung", 15000, 5)
    item1.pay_rate = 0.5
    assert item1.pay_rate == 0.5
    item1.apply_discount()
    assert item1.price == 5000
    assert item2.price == 15000
    assert Item.all == [item1, item2]


"""
Тесты для ДЗ 13.2 homework_2
"""


# TestCase_1 : property , name.getter name.setter
def test_property_name():
    item1 = Item("samsung", 10000, 5)
    item2 = Item("playstation5", 12500, 2)
    assert item1.name == "samsung"
    item1.name = "macbook"
    assert item1.name == "macbook"
    item1.name = "samsung galaxy gt one"
    assert item1.name == "samsung ga"
    assert item2.name == "playstatio"


# TestCase_2 : classmethod instantiate_from_csv
def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[3].name == "Мышка"
    assert Item.all[4].name == "Клавиатура"


# TestCase_3 : staticmethod string_to_number
def test_string_to_number():
    assert Item.string_to_number("4") == 4
    assert Item.string_to_number("4.0") == 4
    assert Item.string_to_number("4.9") == 4


"""
Homework-3 TestCase
"""


# TestCase repr
def test_item_repr():
    item1 = Item("Samsung 10", 10000, 5)
    assert repr(item1) == "Item('Samsung 10', 10000, 5)"


# TestCase str
def test_item_str():
    item1 = Item("Samsung 10", 10000, 5)
    assert str(item1) == "Samsung 10"


"""
Homework-4 TestCase
"""


# TestCase add
def test_add():
    item1 = Item("Samsung 10", 10000, 5)
    item2 = Item("Смартфон", 12500, 2)
    assert item1 + item2 == 7
    # assert item1 + 5 == ValueError('Складывать можно только объекты "Item" и дочерние от них.')


"""
Homework-6 TestCase
"""


# TestCase ValueError
def test_quantity_setter_value_error():
    item1 = Item("Samsung 10", 10000, 5)
    item1.quantity = 0
    assert item1.quantity == 0
    with pytest.raises(ValueError):
        item1.quantity = -4


def test_add_ValueError():
    item1 = Item("Samsung 10", 10000, 5)
    with pytest.raises(ValueError):
        item1 + 4


def test_instantiate_from_csv_error_1():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(
            path=os.path.join(os.path.dirname(__file__), "..", "src", "items2.csv"))

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(
            path=os.path.join(os.path.dirname(__file__), "..", "src", "items3.csv"))

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(
            path=os.path.join(os.path.dirname(__file__), "..", "src", "items4.csv"))


# TestCase InstantiateCSVError
def test_instantiatecsverror():
    value_error = InstantiateCSVError()
    assert str(value_error) == "_Файл item.csv поврежден_"