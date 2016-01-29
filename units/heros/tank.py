# TODO: program hability 2

import random
from units.heros.hero import Hero

class Tank(Hero):
    """
        Hero: Tank
    """

    """
        calculates when the hero attacks first or not

        @return {boolean} True when yes, False when not
    """
    def attacksFirst(self, turnNumber = 1):
        return False

    """
        handles the units receiving attack

        calculates missing chances, armor reduction, etc.
        reduces hp when damage is received

        {hability}: .95 chance to block half damage

        @param {float} incoming damage
        @return {float} damage received or -1.0 when blocked
    """
    def receiveDamage(self, incomingDamage):
        # .10 chance to block half damage
        if random.randint(1,5) == 1:
          # blocks .95, only receives .05
          print('BLOCKED!!!')
          incomingDamage = incomingDamage * 0.05
        # calculate the damage received
        receivedDamage = incomingDamage * self.damageMultiplier()
        # modify hp accordiong to it
        self.hp -= receivedDamage
        # set dead state when hp < 0
        if self.hp <= 0:
            self.dead = True
        return receivedDamage
