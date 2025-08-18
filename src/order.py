from src.base import ForProducts
from typing import Optional, List
from src.product import Product

class Order(ForProducts):
    """Заказ: ровно один товар + его количество + итоговая стоимость."""

    def __init__(self, product: Optional[Product] = None, quantity: int = 0) -> None:
        self.product: Optional[Product] = None
        self.quantity: int = 0
        if product is not None:
            self.add_product(product)

    def __str__(self) -> str:
        if self.product is None:
            return "Пустой заказ"
        return f"Заказ: {self.product.name}, {self.quantity} шт.: {self.product.price * self.quantity} руб."

    def add_product(self, product: Product, /, **kwargs: object) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только Product")
        if self.product is not None:
            raise ValueError("В заказ уже добавлен товар")
        else:
            self.product = product
            self.quantity = 1

    @property
    def products_list(self) -> List[Product]:
        return [self.product] if self.product else "В заказе отсутствует товар"

if __name__ == '__main__':
    order1 = Order()
    print(order1)

    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order1 = Order(product2)
    print(order1)