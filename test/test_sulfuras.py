from olivanders_kata.items import Sulfuras


def test_crear_sulfuras():
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    assert sulfuras.get_name() == "Sulfuras, Hand of Ragnaros"
    assert sulfuras.get_sell_in() == 0
    assert sulfuras.get_quality() == 80


def test_to_string():
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    print("Sulfuras toString() test")
    print(sulfuras)


def test_update_quality_sulfuras():
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    sulfuras.update_quality()
    assert sulfuras.get_sell_in() == 0
    assert sulfuras.get_quality() == 80
