from olivanders_kata.items import NormalItem


def test_crear_normal_item():
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    assert normal.get_name() == "+5 Dexterity Vest"
    assert normal.get_sell_in() == 10
    assert normal.get_quality() == 20


def test_to_string():
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    print(normal)


def test_update_quality_normal_item():
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    normal.update_quality()
    assert normal.get_sell_in() == 9
    assert normal.get_quality() == 19


def test_update_quality_normal_item_expired():
    normal = NormalItem("+5 Dexterity Vest", 0, 20)
    normal.update_quality()
    assert normal.get_sell_in() == -1
    assert normal.get_quality() == 18


def test_quality_min_zero():
    normal = NormalItem("+5 Dexterity Vest", 10, 0)
    normal.update_quality()
    assert normal.get_sell_in() == 9
    assert normal.get_quality() == 0
