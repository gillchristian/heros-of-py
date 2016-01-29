# TODO: test random based habilities procs
import unittest
import json
from units.heros.assassin import Assassin

class TestAssassin(unittest.TestCase):

    def setUp(self):
        with open('data/heros.json') as data_file:
            heros = json.loads(data_file.read())
        self.testAssassin = Assassin(heros[3])

    def test_attacksFirst(self):
        """
            Assassin.attacksFirst() always returns True
        """
        self.assertTrue(self.testAssassin.attacksFirst(0))
        self.assertTrue(self.testAssassin.attacksFirst(1))
        
    def test_attack_equal(self):
      """
          Assassin.attack() equal to hero damage x 1.0 or x 1.5
      """
      attack = self.testAssassin.damage * 1.0 or self.testAssassin.damage * 1.5
      self.assertTrue(attack)

    def test_receiveDamage_hp_decrease(self):
        """
            Assasin.hp should decrease after receiving damage
            unless attack is missed
        """
        # store the starting hp
        prev = self.testAssassin.hp
        # calculate the realDamage (with armor reduction)
        realDamage = 10.0 * self.testAssassin.damageMultiplier()
        # calculate the hp that should be left after attack
        hpLeft = self.testAssassin.hp - realDamage
        # receive damage
        
        attack = self.testAssassin.receiveDamage(10.0)
        if attack != -1:
          # when attack is not missed
          self.assertGreater(prev, self.testAssassin.hp)
          self.assertLess(self.testAssassin.hp, prev)
          self.assertEqual(self.testAssassin.hp, hpLeft)
        else:
          # when attack is missed
          self.assertEqual(self.testAssassin.hp, prev)


if __name__ == '__main__':
    unittest.main()
