from units.monsters.monster import Monster
from helpers.interface import Interface
from handlers.round import Round
import json
import random


class World(object):
    """
        handles world
    """

    # TODO: init method, separation of concerns and new methods
    def __init__(self):
      # load units data
      with open('data/heros.json') as data_file:
        self.heros = json.loads(data_file.read())
      with open('data/monsters.json') as data_file:
        self.monsters = json.loads(data_file.read())

    """
        starts the game, lets the player picks the hero class
    """
    def startGame(self):
      id = Interface.classPick(4)
      self.createHero(id)
      Interface.greetPick(self.hero.name)

    """
        pick a monster and fight agains it
    """
    def fightaMonster(self):
      # pick a random monster
      monsterId = random.randint(0,2)
      self.monster = Monster(self.monsters[monsterId])
      # fight!
      print('\n---------------------')
      print( '{0} vs. {1}'.format(self.hero.name, self.monster.name) )
      print('FIGHT!')
      turn = Round(self.hero, self.monster)
      turn.fight()
        
    """
        creates a hero
    """
    def createHero(self, id):
      if id == 0:
        from units.heros.archer import Archer
        self.hero = Archer(self.heros[id])
        return
      if id == 1:
        from units.heros.fighter import Fighter
        self.hero = Fighter(self.heros[id])
        return
      if id == 2:
        from units.heros.tank import Tank
        self.hero = Tank(self.heros[id])
        return
      if id == 3:
        from units.heros.assassin import Assassin
        self.hero = Assassin(self.heros[id])
        return

    """
        runs a level, figths a desired amount of monsters
        @return {boolean} whether or not the hero won
    """
    def level(self, monstersToFight):
      if monstersToFight == 0:
        isDead = self.hero.isDead()
        if isDead:
          print('\nWhat a bummer, you died and lost!')
        else:
          print('\nCongrats! you killed the last monster and won the level!')
        # return the oposite to isDead
        return not isDead
      else:
        self.fightaMonster()
        if self.hero.isDead():
          print('\nWhat a bummer, you died and lost!')
          return False
        # TODO: random quotes class
        if monstersToFight > 1:
          if random.randint(0,1) == 1:
            againMessage = ', lets fight again!'
          else:
            againMessage = ', look there comes another one!'
          print('\nCongrats! you killed a monster{0}'.format(againMessage) )
        self.level(monstersToFight - 1)
        