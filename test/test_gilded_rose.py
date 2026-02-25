import pytest

from olivanders_kata.gilded_rose import GildedRose
from olivanders_kata.items import NormalItem, AgedBrie


@ pytest.fixture

def setup_inventory():
    shop = GildedRose()
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    brie = AgedBrie("Aged Brie", 2, 0)
    return shop, normal, brie


def test_to_string(setup_inventory):
    shop, normal, brie = setup_inventory
    shop.add_item(brie)
    brie = AgedBrie("Aged Brie", 10, 10)
    shop.add_item(brie)
    print("toString() GildedRose test:")
    print(shop)


def test_add_item(setup_inventory):
    shop, normal, brie = setup_inventory
    shop.add_item(normal)
    shop.add_item(brie)
    assert len(shop.inventory()) == 2
    assert shop.inventory() == [normal, brie]

    print("GildedRose addItem test:")
    print(shop)


def test_update_quality(setup_inventory):
    shop, normal, brie = setup_inventory
    shop.add_item(normal)
    shop.add_item(brie)
    assert len(shop.inventory()) == 2
    print("Dia 0:\n" + str(shop))
    shop.update_quality()

    item = shop.inventory()[0]
    assert item.get_quality() == 19
    assert shop.inventory()[1].get_quality() == 1
    print("Dia 1:\n" + str(shop))
