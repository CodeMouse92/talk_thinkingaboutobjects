"""Classes are defined by their constituent data."""

class Animal:
    # Make immutable --->
    __slots__ = (
        'name',
        'gender',
        'breed',
        'species',
        '__dict__',
        '__weakref__'
    )

    def __setattr__(self, name, value):
        if hasattr(self, name) and name in self.__slots__:
            raise AttributeError(
                f"'{type(self)}' object attribute '{name}' is read-only."
            )
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if hasattr(self, name) and name in self.__slots__:
            raise AttributeError(
                f"'{type(self)}' object attribute '{name}' is read-only."
            )
        object.__delattr__(self, name)

    def __hash__(self):
        return hash(''.join((
            self.name,
            self.gender,
            self.breed,
            self.species
        )))

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.gender == other.gender
            and self.breed == other.breed
            and self.species == other.species
        )

    # <---- Make immutable

    def __init__(self, name, gender, age, breed, species):
        self.name = name
        self.gender = gender
        self.species = species
        self.age = age
        self.breed = breed
        self._notes = []

    def __str__(self):
        string = (
            f"{self.name} is a {self.age} {self.gender} "
            f"{self.breed} {self.species}."
        )
        string = " ".join((string, *self._notes))
        return string

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, note):
        self._notes.append(note.capitalize())
