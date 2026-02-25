from olivanders_kata.items import Conjured


def test_crear_conjured():
    conjured = Conjured("Conjured Mana Cake", 3, 6)
    assert conjured.get_name() == "Conjured Mana Cake"
    assert conjured.get_sell_in() == 3
    assert conjured.get_quality() == 6


def test_to_string():
    conjured = Conjured("Conjured Mana Cake", 3, 6)
    print("toString() Conjured test:")
    print(conjured)


def test_update_quality_conjured():
    conjured = Conjured("Conjured Mana Cake", 3, 6)
    conjured.update_quality()
    assert conjured.get_sell_in() == 2
    assert conjured.get_quality() == 4


def test_update_quality_conjured_just_expired():
    conjured = Conjured("Conjured Mana Cake", 0, 6)
    conjured.update_quality()
    assert conjured.get_sell_in() == -1
    assert conjured.get_quality() == 2


def test_update_quality_conjured_expired():
    conjured = Conjured("Conjured Mana Cake", -1, 6)
    conjured.update_quality()
    assert conjured.get_sell_in() == -2
    assert conjured.get_quality() == 2


def test_quality_min_zero():
    brie = Conjured("Conjured Mana Cake", 1, 1)
    brie.update_quality()
    assert brie.get_sell_in() == 0
    assert brie.get_quality() == 0

    brie = Conjured("Conjured Mana Cake", -1, 0)
    brie.update_quality()
    assert brie.get_sell_in() == -2
    assert brie.get_quality() == 0
