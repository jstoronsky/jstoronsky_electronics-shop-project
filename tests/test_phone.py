import pytest

from src.phone import Phone


def test_repr_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone2 = Phone("iPhone SE", 50000, 5, 1)
    assert phone2.number_of_sim == 1
    with pytest.raises(ValueError, match=r"Количество физических SIM-карт должно быть целым числом больше нуля"):
        phone2.number_of_sim = 0
