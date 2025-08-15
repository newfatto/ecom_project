from typing import List

from src.product import Product


class Category:
    """Класс Категория"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализация экземпляра класса Категория"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Строковое отображение информации о категории для пользователя"""
        products_quantity = 0
        for product in self.__products:
            products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {products_quantity} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращает строку с информацией о продуктах в категории"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_list(self) -> list:
        """Геттер возвращает список с информацией о продуктах в категории"""
        return self.__products
