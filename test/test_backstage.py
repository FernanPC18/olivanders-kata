from olivanders_kata.items import Backstage


def test_crear_backstage():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    assert pass_item.get_name() == "Backstage passes to a TAFKAL80ETC concert"
    assert pass_item.get_sell_in() == 15
    assert pass_item.get_quality() == 20


def test_to_string():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    print("toString() Backstage test")
    print(pass_item)


def test_update_quality_over_ten():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == 14
    assert pass_item.get_quality() == 21


def test_update_quality_over_five():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 6, 20)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == 5
    assert pass_item.get_quality() == 22


def test_update_quality_over_zero():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == 4
    assert pass_item.get_quality() == 23


def test_update_quality_pass_expired():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == -1
    assert pass_item.get_quality() == 0


def test_quality_max_50():
    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == 4
    assert pass_item.get_quality() == 50

    pass_item = Backstage("Backstage passes to a TAFKAL80ETC concert", 9, 49)
    pass_item.update_quality()
    assert pass_item.get_sell_in() == 8
    assert pass_item.get_quality() == 50
