import pytest

from src.iterator import ProductIterator


def test_iterator_iter(product_iterator: ProductIterator) -> None:
    """Проверяет, что __iter__ возвращает сам итератор."""
    assert iter(product_iterator) is product_iterator


def test_iterator_next(product_iterator: ProductIterator) -> None:
    """После обхода всех элементов next() должен выбрасывать StopIteration."""
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)
