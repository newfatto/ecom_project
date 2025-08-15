import json
from pathlib import Path

import pytest

from src.category import Category
from src.iterator import ProductIterator
from src.product import Product


@pytest.fixture
def product1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category1() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций " "для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def product_iterator(category1: Category) -> ProductIterator:
    return ProductIterator(category1)


@pytest.fixture
def sample_data(tmp_path: Path) -> Path:
    """Создаёт временный json-файл с тестовыми данными"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Для связи и жизни",
            "products": [
                {"name": "Xiaomi 13", "description": "128GB", "price": 55000.0, "quantity": 10},
                {"name": "Samsung A54", "description": "256GB", "price": 68000.0, "quantity": 7},
            ],
        }
    ]
    file_path = tmp_path / "test_products.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return file_path
