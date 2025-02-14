

#Created the Pet class,like petco is to petsmart
class Pet:
    # Made store (not like pet store (petsmart) like storage store) for  diffent pets
    species = ""  # This is where I store (not petsmart) the pet's type (like dog, cat, gecko.)
    
    #Set the pet's name, age, and species
    def __init__(self, name, age, species):
        self.name = name  
        self.age = age    
        self.species = species  # The pet's type ( gecko (my fav), dog, cat)
     
    def age_in_human_years(self):
        if self.species.lower() == "dog":
            return self.age * 7  # Dogs age 7 times faster than humans
        elif self.species.lower() == "cat":
            return self.age * 6  # Cats age 6 times faster than humans
        elif self.species.lower() == "geko":
            return self.age * 8  # gecko age 8 times faster than humans (but mine will live forever)
        else:
            return self.age  # For other species, we'll just return the pet's age (no conversion)

    #  Average lifespan of a Dog math and cat (dogs better)
    def average_lifespan(self):
        if self.species.lower() == "dog":
            return 13  
        elif self.species.lower() == "cat":
            return 15  
        else:
            return 10  # most other things won't live ten more years, at least not with my famiy

# Creating three different pets
pet1 = Pet("Spot", 4, "Dog")
pet2 = Pet("Devil", 3, "Cat")
pet3 = Pet("monkey", 5, "gecko")  # monkey is the name of my gecko
pet4 = Pet("Andy", 12, "Lion") #chose lion cause andy is a king

# Print their age in human years and average lifespan
print(f"{pet1.name} (a {pet1.species}) is {pet1.age_in_human_years()} years old in human years.")
print(f"The average lifespan of a {pet1.species} is {pet1.average_lifespan()} years.")

print(f"{pet2.name} (a {pet2.species}) is {pet2.age_in_human_years()} years old in human years.")
print(f"The average lifespan of a {pet2.species} is {pet2.average_lifespan()} years.")

print(f"{pet3.name} (a {pet3.species}) is {pet3.age_in_human_years()} years old in human years.")
print(f"The average lifespan of a {pet3.species} is {pet3.average_lifespan()} years.")

