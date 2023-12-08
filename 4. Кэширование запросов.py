from typing import Any, Tuple


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_data = {}
        self.order = []

    @property
    def cache(self) -> Any:
        if self.order:
            key = self.order[0]
            return key, self.cache_data[key]

    @cache.setter
    def cache(self, new_elem: Tuple[Any, Any]) -> None:
        key, value = new_elem

        if key in self.cache_data:
            self.order.remove(key)
            del self.cache_data[key]

        self.cache_data[key] = value
        self.order.append(key)

        if len(self.cache_data) > self.capacity:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]

    def get(self, key: Any) -> Any:
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]

    def print_cache(self) -> None:
        print("LRU Cache:")
        for key in self.order:
            print(f"{key} : {self.cache_data[key]}")


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2"))  # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
