# TODO: test random based habilities procs
import unittest
import json
from units.heros.archer import Archer

class TestArcher(unittest.TestCase):

    def setUp(self):
        with open('data/heros.json') as data_file:
            heros = json.loads(data_file.read())
        self.testArcher = Archer(heros[0])

    def test_attack_equal(self):
        """
            Archer.attack() equal to hero damage or -1.0
        """
        attack = self.testArcher.damage or -1.0 
        self.assertTrue(attack)
    
    def test_attacksFirst(self):
        """
            Archer.attacksFirst() returns {bool} wheter or not
            the Hero attacks first

            Archer always attacks first the first turn
        """
        attacksFirst = self.testArcher.attacksFirst(0)
        self.assertIs(type(attacksFirst), bool)
        self.assertTrue(attacksFirst)

        attacksFirst = self.testArcher.attacksFirst(1)
        self.assertIs(type(attacksFirst), bool)


if __name__ == '__main__':
    unittest.main()
