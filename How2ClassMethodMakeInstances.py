class Organism():
    def __init__(self,species):
        self.species = species
    def reproduce(cls,species):
        return cls(species)

Dog = Organism('dog')
print(Dog.species)
OtherDog = Organism.reproduce(Organism,'dog')
print(OtherDog.species)
FirstCat = Organism.reproduce(Organism,'cat')
print(FirstCat.species)
