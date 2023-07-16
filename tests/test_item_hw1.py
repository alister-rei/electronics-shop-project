from src.item import Item


# Тесты для проверки класса
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
