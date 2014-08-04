

class Animal:
    animalCount = 0 

    def __init__(self, numberOfLegs, color, presenceOfFur, weight, length, species, name):
            self.numberOfLegs = numberOfLegs
            self.color = color
            self.presenceOfFur = presenceOfFur
            self.weight = weight
            self.length = length
            self.species = species
            self.name = name

    def displayAnimalInfo(self):
            print "Legs:", self.numberOfLegs
            print "Color:", self.color
            print "Fur:", self.presenceOfFur
            print "Weight:", self.weight
            print "Length:", self.length
            print "Species:", self.species
            print "Name:", self.name
           

    def displayNumAnimals(self):
            print "Total Animals:", Animal.animalCount

    def sleep(self):
        print self.name, "the", self.species, "is sleeping"

    def breathe(self):
        print self.name, "the", self.species, "is breathing"

    def walk(self):
        print self.name,"the", self.species, "is walking"

dog = Animal(4, "Brown", "True", 24,36, "Canine", "Roofus")
cat = Animal(4, "Grey", "True", 7, 27, "Feline", "Mischief")

print "Dog:"
dog.displayAnimalInfo()
print "Cat:"
cat.displayAnimalInfo()

dog.sleep(), dog.breathe(), dog.walk()
cat.sleep(), cat.breathe(), cat.walk()

