class Product:
    """Класс Продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация экземпляра класса Продукт"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
