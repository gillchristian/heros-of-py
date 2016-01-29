# TODO: program hability 2

import random
from units.heros.hero import Hero

class Archer(Hero):
    """
        Hero: Archer
    """

    """
        handles the units attack

        {hability}: .10 chance to kill by one shot

        @return {float} self damage, or -1.0 when headshot
    """
    def attack(self, turnNumber):
        if random.randint(1,10) == 1:
            print('Lucky headshot!!!')
            return -1.0
        return self.damage

    """
        calculates when the hero attacks first or not

        @return {boolean} True when yes, False when not
    """
    def attacksFirst(self, turnNumber = 0):
        if turnNumber == 0:
            return True
        if random.randint(0,1):
            return True
        else:
            return False
