from typing import Any, Dict, List, Optional


class Product:
    """Класс Продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса Продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
