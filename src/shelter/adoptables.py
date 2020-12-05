import sys
from collections.abc import Collection


class Adoptables(Collection):

    def __init__(self):
        self._adoptable = set()

    def add(self, animal):
        self._adoptable.add(animal)

    def mark_adopted(self, animal):
        try:
            self._adoptable.remove(animal)
        except ValueError:
            print("Already adopted.", file=sys.stderr)

    def __iter__(self):
        return iter(self._adoptable)

    def __contains__(self, animal):
        return animal in self._adoptable

    def __len__(self):
        return len(self._adoptable)


adoptables = Adoptables()
