from src.keyboard import Keyboard


#TestCase #1 class keyboard init
def test_keyboard_init():
    key = Keyboard('Defender Wired keyboard', 1500, 7)
    assert key.name == 'Defender Wired keyboard'
    assert key.price == 1500.0
    assert key.quantity == 7

#TestCase #2 test change_leng
def test_change_lang():
    key = Keyboard('Defender Wired keyboard', 1500, 7)
    assert key.language == "EN"
    key.change_lang()
    assert key.language == "RU"
    key.change_lang().change_lang()
    assert key.language == "RU"
