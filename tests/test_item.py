from src.item import Item


def test_item():
    item1 = Item("Смартфон", 10000, 10)
    item2 = Item("Samsung", 15000, 5)

    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 10

    assert item1.calculate_total_price() == 100000

    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000
    assert item2.price == 15000

    assert Item.all == [item1, item2]

