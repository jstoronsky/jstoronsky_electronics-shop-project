"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_item_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    if item.name == "СуперСмартфон":
        assert item.name == 'Смартфон'


def test_item_all():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[2]
    assert item1.name == 'Кабель'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('10.3') == 10


def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add():
    item2 = Item("Смартфон", 10000, 20)
    phone2 = Phone("iPhone SE", 50000, 5, 1)
    assert item2 + phone2 == 25
    assert phone2 + item2 == 25
    assert phone2 + phone2 == 10
    assert item2 + item2 == 40
    assert item2 + 5 is None
    assert phone2 + 3 is None
