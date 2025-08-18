import pytest

from src.category import Category
from src.product import Product


def test_category_init(category1: Category) -> None:
    """Тестирование корректной инициализации класса Категория"""
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products.count("руб. Остаток:") == 3

    assert category1.category_count == 1
    assert category1.product_count == 3


def test_add_product(category1: Category) -> None:
    """Тестирование добавления продукта в категорию"""
    initial_count = category1.product_count
    new_product = Product("Новый телефон", "Описание нового телефона", 50000.0, 2)
    category1.add_product(new_product)

    assert category1.products.count("руб. Остаток:") == 4
    assert "Новый телефон" in category1.products
    assert category1.product_count == initial_count + 1


def test_products_property(category1: Category) -> None:
    """Тестирование свойства products"""
    products_str = category1.products
    assert isinstance(products_str, str)

    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "Iphone 15" in products_str
    assert "Xiaomi Redmi Note 11" in products_str

    assert "руб. Остаток:" in products_str
    assert "шт." in products_str


def test_category_counters() -> None:
    """Тестирование счётчиков при создании нескольких категорий"""
    Category.category_count = 0
    Category.product_count = 0

    products1 = [Product("Продукт 1", "Описание 1", 100.0, 1)]
    category1 = Category("Категория 1", "Описание категории 1", products1)  # noqa: F841

    assert Category.category_count == 1
    assert Category.product_count == 1
    products2 = [Product("Продукт 2", "Описание 2", 200.0, 2), Product("Продукт 3", "Описание 3", 300.0, 3)]
    category2 = Category("Категория 2", "Описание категории 2", products2)  # noqa: F841

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product_increases_counter(category1: Category) -> None:
    """Тестирование увеличения счётчика при добавлении продукта"""
    initial_product_count = Category.product_count

    new_product = Product("Тестовый продукт", "Описание", 1000.0, 1)
    category1.add_product(new_product)

    assert Category.product_count == initial_product_count + 1


def test_category_add_product(category1: Category) -> None:
    """Тестирование добавления продукта в категорию через создание нового продукта"""
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    category1.add_product(new_product)

    assert "Samsung Galaxy S23 Ultra" in category1.products
    assert category1.products.count("руб. Остаток:") == 4


def test_category_add_product_error(category1: Category) -> None:
    new_product = "не продукт"
    with pytest.raises(TypeError):
        category1.add_product(new_product)  # type: ignore[arg-type]


def test_products_list_returns_list_of_products(category1: Category) -> None:
    """Проверяет, что products_list возвращает список объектов Product в правильном порядке."""
    products = category1.products_list
    assert [p.name for p in products] == [
        "Samsung Galaxy S23 Ultra",
        "Iphone 15",
        "Xiaomi Redmi Note 11",
    ]


def test_category_str(category1: Category) -> None:
    """Тест проверяет корректное строковое отображение категории для пользователя"""
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."
