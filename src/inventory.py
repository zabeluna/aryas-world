# src/inventory.py

class Inventory:
    def __init__(self):
        self._items = []  # Lista de strings (nomes dos itens)

    def add_item(self, name: str):
        self._items.append(name)
        self._items = self._quicksort(self._items)

    def count(self, name: str) -> int:
        return self._items.count(name)

    def all_items(self) -> list:
        return self._items[:]

    def filter_by(self, name: str) -> list:
        return [i for i in self._items if i == name]

    # ── QuickSort ────────────────────────────────────────────────
    def _quicksort(self, lst: list) -> list:
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]
        left   = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right  = [x for x in lst if x > pivot]
        return self._quicksort(left) + middle + self._quicksort(right)

    def __repr__(self):
        return f"Inventory({self._items})"