import unittest
import json
from handlers.round import Round
from units.monsters.monster import Monster
from units.heros.hero import Hero

class TestTurn(unittest.TestCase):

    def setUp(self):
      with open('data/monsters.json') as data_file:
        monsters = json.loads(data_file.read())
        self.testMonster = Monster(monsters[0])
      with open('data/heros.json') as data_file:
        heros = json.loads(data_file.read())
        self.testHero = Hero(heros[1])

      self.testTurn= Round(self.testHero, self.testMonster)
    
    '''
    TODO: test turn
    def test_fight(self):
      self.assertTrue(True)
    '''
if __name__ == '__main__':
    unittest.main()
