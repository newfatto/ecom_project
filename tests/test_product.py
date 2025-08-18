import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.product import LawnGrass, Product, Smartphone


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


def test_smartphone_init(smartphone1: Smartphone) -> None:
    """Проверка корректной инициализации класса Смартфон"""
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    """Провверка корректного сложение двух экземпляров класса Смартфон"""
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphone_add_error(smartphone1: Smartphone) -> None:
    """Проверка возникновения ошибки при попытке сложения экземпляра класса LawnGrass с другим объектом"""
    with pytest.raises(TypeError):
        smartphone1 + 1  # type: ignore[operator]


def test_lawngrass_init(grass1: LawnGrass) -> None:
    """Проверка корректной инициализации класса LawnGrass"""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == ("Зеленый")


def test_lawngrass_add(grass1: LawnGrass, grass2: LawnGrass) -> None:
    """Проверка корректности сложения двух экземпляров класса LawnGrass"""
    assert grass1 + grass2 == 16750.0


def test_lawngrass_add_error(grass1: LawnGrass) -> None:
    """Проверка возникновения ошибки при попытке сложения экземпляра класса LawnGrass с другим объектом"""
    with pytest.raises(TypeError):
        grass1 + 1  # type: ignore[operator]
