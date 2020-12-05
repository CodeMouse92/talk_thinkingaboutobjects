"""Animal Adoption
Present animals who are up for adoption.
Automate adoption process.
"""

from .adoptables import adoptables
from .animal import Animal
from .adopter import Adopter


def display_animals(adoptables):
    for animal in adoptables:
        print(animal)


def verify_adopter(adopter):
    print(f"Checking identity on {adopter.name}")
    return True


def process_payment(adopter):
    print(f"Get payment info from {adopter.name}")


def register_animal(animal, adopter):
    print(f"Register {animal.name} to {adopter.name}.")
    return True


def adopt(animal, adopter, adoption_pool=adoptables):
    if animal in adoption_pool and verify_adopter(adopter):
        process_payment(adopter)
        register_animal(animal, adopter)
        adoption_pool.mark_adopted(animal)


def main():
    fluffy = Animal(
        name="Fluffy",
        species="cat",
        gender="female",
        age="1-yr-old",
        breed="Maine coon",
    )
    fluffy.notes = "hates dogs"

    adoptables.add(fluffy)

    butch = Animal(
        name="Butch",
        species="dog",
        gender="male",
        age="1-yr-old",
        breed="mutt/coyote mix",
    )
    butch.notes = "enthusiastic, friendly."
    butch.notes = "dumb as a rock."
    adoptables.add(butch)

    display_animals(adoptables)

    adopter = Adopter(
        name="Jason C. McDonald",
        gov_id='12345',
        address='123 Anywhere St.',
        phone='555-1234',
        email='codemouse92@outlook.com'
    )

    adopt(butch, adopter)
