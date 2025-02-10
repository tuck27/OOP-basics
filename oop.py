import random

class Character:
    #class attributes
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Telekenesis", "Invisibility", "Teleportation", "Flying", "Super Strength"]

    #Constructor
    def __init__(self):
        self.generate_character()

    #this is a method
    def generate_character(self):
        self.hair_color = random.choice(Character.hair_colors)
        self.size = random.choice(Character.sizes)
        self.special_power = random.choice(Character.special_powers)
        self.description = (
            f"Your character has {self.hair_color} hair, "
            f"is {self.size} in size, and has the power of {self.special_power}"
        )

    def __str__(self):
        return self.description

char1 = Character()
char2 = Character()

print(char1)
print(char2)