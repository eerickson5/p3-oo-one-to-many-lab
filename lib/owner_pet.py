class Pet:
    def __init__(self, name, pet_type, owner = None):
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.name = name
        self.owner = owner
        Pet.all.append(self)
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        pet.owner = self

    def get_sorted_pets(self):
        pets = self.pets()
        pets.sort(key = lambda pet: pet.name)
        return pets