import pytest
from src.order import Order
from src.product import Product


def test_order_empty_str() -> None:
    o = Order()
    assert str(o) == "Пустой заказ"
    assert o.product is None
    assert o.quantity == 0
    assert o.products_list == "В заказе отсутствует товар"


def test_order_init_with_product(product2: Product) -> None:
    o = Order(product2)
    assert o.product is product2
    assert o.quantity == 1
    assert o.products_list == [product2]
    assert str(o) == f"Заказ: {product2.name}, 1 шт.: {product2.price * 1} руб."


def test_order_add_product_sets_fields(product1: Product) -> None:
    o = Order()
    o.add_product(product1)
    assert o.product is product1
    assert o.quantity == 1
    assert o.products_list == [product1]
    assert "Заказ:" in str(o)


def test_order_add_product_twice_raises(product1: Product) -> None:
    o = Order(product1)
    with pytest.raises(ValueError):
        o.add_product(product1)


def test_order_add_wrong_type_raises() -> None:
    o = Order()
    with pytest.raises(TypeError):
        o.add_product("не продукт")  # type: ignore[arg-type]
