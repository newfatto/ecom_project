from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


def test_product_init(product1: Product) -> None:
    """Тестируем правильную инициализацию"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product_adds_to_existing() -> None:
    """Если продукт с таким именем уже есть — обновляется"""
    category_list = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [{"name": "Iphone 15", "description": "512GB", "price": 120000.0, "quantity": 2}],
        }
    ]
    new_data = {"name": "Iphone 15", "description": "512GB", "price": 125000.0, "quantity": 3}

    product = Product.new_product(new_data, category_list)

    assert product.name == "Iphone 15"
    assert product.price == 125000.0
    assert product.quantity == 5


def test_new_product_creates_new() -> None:
    """Создаётся новый продукт, если его нет в списке"""
    new_data = {"name": "Nothing Phone 2", "description": "128GB, Black", "price": 80000.0, "quantity": 10}

    product = Product.new_product(new_data)

    assert isinstance(product, Product)
    assert product.name == "Nothing Phone 2"
    assert product.price == 80000.0
    assert product.quantity == 10


def test_price_setter_rejects_negative(product1: Product) -> None:
    """Если цена отрицательная — не изменяется"""
    original_price = product1.price
    product1.price = -1000.0
    assert product1.price == original_price


def test_price_setter_confirms_decrease(monkeypatch: MonkeyPatch) -> None:
    """Пользователь подтверждает снижение цены"""
    product = Product("Test Phone", "Описание", 90000.0, 2)

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 85000.0

    assert product.price == 85000.0


def test_price_setter_declines_decrease(monkeypatch: MonkeyPatch) -> None:
    """Пользователь отказывается снижать цену"""
    product = Product("Test Phone", "Описание", 90000.0, 2)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 85000.0

    assert product.price == 90000.0


def test_product_str(product1: Product) -> None:
    """Тест проверяет корректное строковое отображение продукта для пользователя"""
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    """Тест проверяет корректное сложение стоимости всех элементов двух продуктов"""
    assert product1 + product2 == 2580000.0
