import random
from array import *
from units.heros.hero import Hero
from units.monsters.monster import Monster

from helpers.logger import Logger

class Round(object):
    """
        runs a round
    """

    def __init__(self, hero, monster):
      self.hero = hero
      self.monster = monster
      self.over = False
      self.turnNumber = 0

    """
        runs the round fight
    """
    def fight(self):
      while not self.over:
        self.turn()
        self.turnNumber += 1
        if self.hero.isDead() or self.monster.isDead():
          self.over = True
      # TODO: place this in another place
      # the hero heals after killing a monster
      if not self.hero.isDead():
        self.hero.heal()
      #Logger.health(self.hero, self.monster)

    """
        runs a turn in a fight
    """
    # TODO: REWORK THIS METHOD!
    def turn(self):
      #Logger.health(self.hero, self.monster)
      if self.hero.attacksFirst(self.turnNumber):
        self.monster.receiveDamage( self.hero.attack(self.turnNumber) )
        if not self.monster.isDead():
          self.hero.receiveDamage( self.monster.attack() )
      else:
        self.hero.receiveDamage( self.monster.attack() )
        if not self.hero.isDead():
          self.monster.receiveDamage( self.hero.attack(self.turnNumber) )
