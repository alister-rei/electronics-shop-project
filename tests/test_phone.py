from src.phone import Phone


# TestCase class Phone
def test_init():
    Phone.all.clear()
    phone1 = Phone("Samsung 10", 25000, 5, 2)
    assert phone1.name == "Samsung 10"
    assert phone1.price == 25000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    assert phone1.pay_rate == 1.0
    assert str(Phone.all[0]) == "Samsung 10"


def test_number_of_sum():
    phone1 = Phone("Samsung 10", 25000, 5, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    # phone1.number_of_sim = 0
    # assert phone1.number_of_sim == ValueError


def test_repr():
    phone1 = Phone("Samsung 10", 25000, 5, 2)
    assert repr(phone1) == "Phone('Samsung 10', 25000, 5, 2)"
