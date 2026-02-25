from olivanders_kata.items import AgedBrie


def test_crear_aged_brie():
    cheese = AgedBrie("Aged Brie", 2, 0)
    assert cheese.get_name() == "Aged Brie"
    assert cheese.get_sell_in() == 2
    assert cheese.get_quality() == 0


def test_to_string():
    cheese = AgedBrie("Aged Brie", 2, 0)
    print("toString() Aged Brie test:")
    print(cheese)


def test_update_quality_brie():
    cheese = AgedBrie("Aged Brie", 2, 0)
    cheese.update_quality()
    assert cheese.get_sell_in() == 1
    assert cheese.get_quality() == 1


def test_update_quality_brie_expired():
    cheese = AgedBrie("Aged Brie", 0, 0)
    cheese.update_quality()
    assert cheese.get_sell_in() == -1
    assert cheese.get_quality() == 2


def test_quality_max_50():
    brie = AgedBrie("Aged Brie", -1, 50)
    brie.update_quality()
    assert brie.get_sell_in() == -2
    assert brie.get_quality() == 50

    brie = AgedBrie("Aged Brie", -1, 49)
    brie.update_quality()
    assert brie.get_sell_in() == -2
    assert brie.get_quality() == 50
