import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = sorted(roll_dice() for _ in range(4)) #Generates a sorted list with 4 rolled dice
        return sum(rolls[1:]) #Ignores the first(lowest) value and sums those numbers then returns it

def modifier(constitution):
    return (constitution - 10) // 2

def roll_dice():
    return random.randint(1,6) # Rolls a dice