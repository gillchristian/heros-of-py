# TODO: test random based habilities procs
import unittest
import json
from units.heros.tank import Tank

class TestTank(unittest.TestCase):

    def setUp(self):
        with open('data/heros.json') as data_file:
            heros = json.loads(data_file.read())
        self.testTank = Tank(heros[2])


    def test_attacksFirst(self):
        """
            Tank.attacksFirst() returns False always
        """
        self.assertFalse(self.testTank.attacksFirst(0))
        self.assertFalse(self.testTank.attacksFirst(1))

    def test_receiveDamage_hp_decrease(self):
        """
            Tank.hp should decrease after receiving damage
        """
        # store the starting hp
        prev = self.testTank.hp
        # calculate the realDamage (with armor reduction)
        realDamage = 10.0 * self.testTank.damageMultiplier()
        # calculate the hp that should be left after attack
        hpLeft = self.testTank.hp - realDamage
        # receive damage
        attack = self.testTank.receiveDamage(10.0)

        self.assertGreater(prev, self.testTank.hp)
        self.assertLess(self.testTank.hp, prev)
        
        # can not assertEqual because blocked attack is reduced
        # self.assertEqual(self.testTank.hp, hpLeft)
    
    '''
    TODO test hability 2
    def test_receiveDamage_return_damage(self):
        """
            Tank.receiveDamage() should return the received damage
        """
    '''
if __name__ == '__main__':
    unittest.main()
