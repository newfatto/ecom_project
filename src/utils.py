import json
import os
from typing import Any, Dict, List


def read_json(path: str) -> List[Dict[str, Any]] | Any:
    """Функция принимает на вход путь до json-файла, и преобразует его python объект"""
    abs_path = os.path.abspath(path)
    with open(abs_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_objects(data: list) -> list:
    """Функция принимает на вход список с данными, и возвращает список объектов класса Category содержащимися
    в них списком объектов класса Product"""
    # Импортируем классы внутри функции, чтобы избежать циклических импортов
    from src.category import Category
    from src.product import Product

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            category["products"] = products
        categories.append(Category(**category))
    return categories
