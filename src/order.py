from typing import Optional

from src.base import ForProductList
from src.exceptions import ZeroException
from src.product import Product


class Order(ForProductList):
    """Заказ: ровно один товар + его количество + итоговая стоимость."""

    def __init__(self, product: Optional[Product] = None, quantity: int = 1) -> None:
        self.product: Optional[Product] = None
        self.quantity: int = 0
        if product is not None:
            self.add_product(product, quantity=quantity)

    def __str__(self) -> str:
        if self.product is None:
            return "Пустой заказ"
        return f"Заказ: {self.product.name}, {self.quantity} шт.: {self.product.price * self.quantity} руб."

    def add_product(self, product: Product, /, *, quantity: int = 1) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только Product")
        if self.product is not None:
            raise ValueError("В заказ уже добавлен товар")
        try:
            if quantity <= 0:
                raise ZeroException("Невозможно создать заказ с нулевым количеством товара")
            self.product = product
            self.quantity = quantity
            print("Товар добавлен")
        except ZeroException as e:
            print(str(e))
            raise
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products_list(self) -> list[Product] | str:
        return [self.product] if self.product else "В заказе отсутствует товар"
