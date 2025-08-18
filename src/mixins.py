class MixinPrint():
    """
    Миксин-класс, выводит в консоль информацию при инициализации нового экземпляра класса в формате:
    'Product('Продукт1', 'Описание продукта', 'цена', 'количество')'
    """

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{getattr(self, 'name', None)}, {getattr(self, 'description', None)}, "
            f"{getattr(self, 'price', None)}, {getattr(self, 'quantity', None)})"
        )