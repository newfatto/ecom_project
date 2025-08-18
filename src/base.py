from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.product import Product


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass


class ForProductList(ABC):

    @abstractmethod
    def add_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Добавить продукт (в заказ — один, в категорию — в список)."""
        pass

    @property
    @abstractmethod
    def products_list(self) -> list["Product"] | str:
        """Список продуктов (в заказе длина будет 0 или 1)."""
        pass
