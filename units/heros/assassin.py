import random
from units.heros.hero import Hero

class Assassin(Hero):
    """
        Hero: Assassin
    """

    """
        handles the unit attack

        {hability}: .20 chance to do 1.5 x damage

        @return {float} self damage
    """
    def attack(self, turnNumber):
        damageMultiplier = 1.0
        if random.randint(1,5) == 1:
            damageMultiplier = 1.5
            print('1.5x Critical!')
        return self.damage * damageMultiplier

    """
        calculates when the hero attacks first or not

        @return {boolean} True when yes, False when not
    """
    def attacksFirst(self, turnNumber = 1):
        return True

    """
        handles the units receiving attack

        calculates missing chances, armor reduction, etc.
        reduces hp when damage is received

        {hability}: .25 evassion

        @param {float} incoming damage
        @return {float} damage received or -1.0 when missed
    """
    def receiveDamage(self, incomingDamage):
        # .25 evassion
        if random.randint(1,4) == 1:
            print('MISS!')
            return -1
        # calculate the damage received
        receivedDamage = incomingDamage * self.damageMultiplier()
        # modify hp accordiong to it
        self.hp -= receivedDamage
        # set dead state when hp < 0
        if self.hp <= 0:
            self.dead = True
        return receivedDamage
