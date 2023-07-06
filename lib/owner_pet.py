

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__( self, name, pet_type, owner="" ):
        self.name = name
        self.pet_type = pet_type
        if owner != "":
            self.owner = owner
        self.all.append( self )
    
    def get_pet_type( self ):
        return self._pet_type
    
    def set_pet_type( self, pet_type ):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("")

    pet_type = property( get_pet_type, set_pet_type )


class Owner:
    def __init__( self, name ):
        self.name = name
    
    def pets( self ):
        owner_pets = [x for x in Pet.all if x.owner == self]
        return owner_pets

    def add_pet( self, pet ):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("")

    def get_sorted_pets( self ):
        unsorted_pets = self.pets()
        return sorted(unsorted_pets, key=lambda pet: pet.name)
            