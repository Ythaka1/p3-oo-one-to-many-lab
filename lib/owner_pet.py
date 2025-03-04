class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  
        Pet.all.append(self)

        if owner:  
            self.set_owner(owner)

    def set_owner(self, owner):
        if isinstance(owner, Owner):
            self.owner = owner
            owner.add_pet(self)  
        else:
            raise TypeError("Owner must be an instance of Owner.")

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet) and pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self  
        else:
            raise TypeError("Only instances of Pet can be added.")

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
