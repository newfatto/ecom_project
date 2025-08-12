from pathlib import Path

from src.category import Category
from src.utils import get_objects, read_json


def test_read_json_reads_data(sample_data: Path) -> None:
    """Проверяет чтение json"""
    result = read_json(str(sample_data))
    assert isinstance(result, list)
    assert result[0]["name"] == "Смартфоны"
    assert len(result[0]["products"]) == 2


def test_get_objects_creates_categories() -> None:
    """Проверяет, что get_objects создаёт объекты Category и Product"""
    input_data = [
        {
            "name": "Ноутбуки",
            "description": "Для работы",
            "products": [
                {"name": "Lenovo ThinkPad", "description": "i5, 8GB", "price": 75000.0, "quantity": 5},
                {"name": "HP EliteBook", "description": "i7, 16GB", "price": 88000.0, "quantity": 3},
            ],
        }
    ]

    categories = get_objects(input_data)

    assert isinstance(categories, list)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)

    products_text = categories[0].products
    assert "Lenovo ThinkPad" in products_text
    assert "HP EliteBook" in products_text
    assert products_text.count("руб. Остаток:") == 2
