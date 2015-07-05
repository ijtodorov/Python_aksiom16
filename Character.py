__author__ = 'Cib'
import json



class character():
    def __init__(self, filename):
        with open(filename) as data_file:
            statistics = json.load(data_file)
        self.strength=statistics["strength"]
        self.dexterity=statistics["dexterity"]
        self.intelligence=statistics["intelligence"]
        self.precision=statistics["precision"]
        self.toughness=statistics["toughness"]
        self.name=statistics["name"]
        self.level=statistics["level"]
        self.vitality=statistics["vitality"]
        self.speed=statistics["speed"]
        self.magicResistance=statistics["magicResistance"]
        self.MPmax=(self.speed+self.dexterity)/2
        self.MP=self.MPmax
        self.magicSkill=(self.intelligence+self.level)/2
        self.magicAttack=self.magicSkill/3
        self.mana=self.intelligence
        self.baseDefense=self.dexterity + self.level/2
        self.baseDamage=10-self.strength
        if self.baseDamage<0:
            self.baseDamage=0


