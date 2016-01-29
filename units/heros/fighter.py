# TODO: program habilities 2 & 3

import random
from units.heros.hero import Hero

class Fighter(Hero):
    """
        Hero: Fighter
    """
    def __init__(self, data):

        self.name = data['name']
        #self.lvl = data['lvl']
        self.hp = data['health']
        self.originalHp = data['health']
        self.damage = data['damage']
        self.starterDamage = data['damage']
        self.armor = data['armor']
        self.habilities = data['habilities']
        self.dead = False


    """
        handles the unit attack

        {hability}: .05 increased damge on each subsecuent attack

        @return {float} self damage
    """
    # TODO: REWORK THIS METHOD
    #       arguments problem with the other methods
    #       newTarget = True solution ?
    def attack(self, turnNumber):
        # never change the actual damage
        if turnNumber == 0:
            # restart self.increasedDamage on first turn
            self.increasedDamage = self.damage
            return self.damage
        else:
            self.increasedDamage += self.increasedDamage * turnNumber * 0.15
            print('Damage increases!!!')
            return self.increasedDamage
