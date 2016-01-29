import json

class Monster(object):
    """
        monster class
    """
    def __init__(self, data):
        self.name = data['name']
        self.lvl = data['lvl']
        self.hp = data['health']
        self.damage = data['damage']
        self.armor = data['armor']
        self.habilities = data['habilities']
        self.dead = False


    """
        handles the units attack

        @return {float} self damage
    """
    def attack(self):
        return self.damage


    """
        handles the units receiving attack

        calculates missing chances, armor reduction, etc.
        reduces hp when damage is received

        @param {float} incoming damage
        @return {float} damage received
    """
    # TODO: rework units interactions
    def receiveDamage(self, incomingDamage):
        # dies automatically when <Archer headshot> triggers
        if incomingDamage == -1.0:
            self.die()
            receivedDamage = self.hp
            self.hp = 0
            return receivedDamage
        # calculate the damage received
        receivedDamage = incomingDamage * self.damageMultiplier()
        # modify hp accordiong to it
        self.hp -= receivedDamage
        # set dead state when hp < 0
        if self.hp <= 0:
            self.die()
        return receivedDamage


    """
        check if is dead
    """
    def isDead(self):
        return self.dead

    """
        calculates the armor damage multiplier
        according to self armor

        @return {float} damage multiplier
    """
    def damageMultiplier(self):
        return 1.0 - 0.06 * self.armor / ( 1 + (0.06 * abs(self.armor) ) )

    """
        set dead state to True
    """
    def die(self):
        self.dead = True
