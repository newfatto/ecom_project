from typing import Any

from src.category import Category


class ProductIterator:

    def __init__(self, category_obj: Category):
        """Инициализирует итератор.
        Args:
            category_obj (Category): объект класса Category
        """
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Возвращает итератор"""
        return self

    def __next__(self) -> Any:
        """Возвращает следующий продукт в категории.
        Returns:
            str: Описание продукта.
        Raises:
            StopIteration: Если достигнута верхняя граница диапазона.
        """
        if self.index < len(self.category_obj.products_list):
            product = self.category_obj.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
