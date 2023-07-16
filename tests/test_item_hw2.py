from src.item import Item
import os

# TestCase_1 : property , name.getter name.setter
def test_property_name():
    item1 = Item("samsung", 10000, 5)
    assert item1.name == "samsung"
    item1.name = "macbook"
    assert item1.name == "macbook"
    item1.name = "samsung galaxy gt one"
    assert item1.name == "samsung ga"

# TestCase_2 : classmethod instantiate_from_csv
# Only from Pytest in terminal from file ...\electronics-shop-project
def test_instantiate_from_csv():
    # относительный путь для проверки через pytest -cov
    path = os.path.join("src", "items.csv")
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[3].name == "Мышка"
    assert Item.all[4].name == "Клавиатура"

# TestCase_3 : staticmethod string_to_number
def test_string_to_number():
    assert Item.string_to_number("4") == 4
    assert Item.string_to_number("4.0") == 4
    assert Item.string_to_number("4.9") == 4

