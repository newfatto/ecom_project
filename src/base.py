from abc import ABC, abstractmethod
from typing import Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.product import Product


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass


class ForProducts(ABC):

    @classmethod
    @abstractmethod
    def add_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Добавить продукт (в заказ — один, в категорию — в список)."""
        pass

    @property
    @abstractmethod
    def products_list(self) -> List["Product"]:
        """Список продуктов (в заказе длина будет 0 или 1)."""
        pass