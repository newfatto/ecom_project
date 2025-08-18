from typing import Any, Dict, List, Optional

from src.base import BaseProduct
from src.mixins import MixinPrint


class Product(BaseProduct, MixinPrint):
    """Класс Продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса Продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Строковое отображение информации о продукте для пользователя"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Получения общей стоимости всех экземпляров двух продуктов"""
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product: Dict[str, Any], category_list: Optional[List[Dict[str, Any]]] = None) -> "Product":
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]

        if category_list:
            for category in category_list:
                for spl_prd in category["products"]:
                    if spl_prd["name"] == name:
                        spl_prd["quantity"] += quantity
                        spl_prd["price"] = max(spl_prd["price"], price)
                        return cls(spl_prd["name"], spl_prd["description"], spl_prd["price"], spl_prd["quantity"])

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_input = input('Вы уверены, что хотите уменьшить стоимость? Если ДА - введите "y": ')
                if user_input == "y":
                    self.__price = new_price
                else:
                    print("Стоимость не изменилась")


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализация экземпляра класса Смартфон"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализация экземпляра класса Смартфон"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
