from src.item import Item
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
    Item.pay_rate = 0.5
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
