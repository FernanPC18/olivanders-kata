from olivanders_kata.items import Item


def test_crear_item():
    item = Item("+5 Dexterity Vest", 10, 20)

    assert item.get_name() == "+5 Dexterity Vest"
    assert item.get_sell_in() == 10
    assert item.get_quality() == 20
    # __str__ should not raise
    print(item)
