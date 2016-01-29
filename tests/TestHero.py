import unittest
import json
import random
from units.heros.hero import Hero

class TestHero(unittest.TestCase):

    def setUp(self):
        with open('data/heros.json') as data_file:
            heros = json.loads(data_file.read())
            index = random.randint(0,3)
            self.testHero = Hero(heros[index])

    def test_attack_equal_own_damage(self):
        """
            Hero.attack() equal to hero damage
        """
        self.assertEqual(self.testHero.attack(0), self.testHero.damage )

    def test_receiveDamage_hp_decrease(self):
        """
            Hero.hp should decrease after receiving damage
        """
        # store the starting hp
        prev = self.testHero.hp
        # calculate the realDamage (with armor reduction)
        realDamage = 10.0 * self.testHero.damageMultiplier()
        # calculate the hp that should be left after attack
        hpLeft = self.testHero.hp - realDamage
        # receive damage
        self.testHero.receiveDamage(10.0)

        self.assertGreater(prev, self.testHero.hp)
        self.assertLess(self.testHero.hp, prev)
        self.assertEqual(self.testHero.hp, hpLeft)

    def test_receiveDamage_set_dead(self):
        """
            Hero should die after receiving letal damage
        """
        self.testHero.hp = 5.0
        self.testHero.receiveDamage(10.0)

        self.assertTrue(self.testHero.dead)

    def test_receiveDamage_return_damage(self):
        """
            Hero.receiveDamage() should return the received damage
        """
        # equal to received damage when armor == 0
        self.testHero.armor = 0
        self.assertEqual(self.testHero.receiveDamage(10.0), 10.0)

        # less than received damage when armor > 0
        self.testHero.armor = 5.0
        self.assertLess(self.testHero.receiveDamage(10.0), 10.0)

        # greater than received damage when armor < 0
        self.testHero.armor = -5.0
        self.assertGreater(self.testHero.receiveDamage(10.0), 10.0)

    def test_damageMultiplier_armor_values(self):
        """
            Hero.damageMultiplier() should return a multiplier according to the self.armor
        """
        # equal to 1.0 when armor == 0
        self.testHero.armor = 0
        self.assertEqual(self.testHero.damageMultiplier(), 1.0)

        # less than 1.0 when armor > 0
        self.testHero.armor = 5.0
        self.assertLess(self.testHero.damageMultiplier(), 1.0)

        # greater than 1.0 when armor < 0
        self.testHero.armor = -5.0
        self.assertGreater(self.testHero.damageMultiplier(), 1.0)

    def test_isDead_and_die(self):
        """
            Hero.die() should set Hero.dead to True
            Hero.isDead() should be equal to Hero.dead
        """
        self.assertFalse(self.testHero.dead)
        self.assertFalse(self.testHero.isDead())
        self.assertEqual(self.testHero.isDead(), self.testHero.dead)

        self.testHero.die()

        self.assertTrue(self.testHero.dead)
        self.assertTrue(self.testHero.isDead())
        self.assertEqual(self.testHero.isDead(), self.testHero.dead)

    def test_attacksFirst(self):
        """
            Hero.attacksFirst() returns {bool} wheter or not
            the Hero attacks first
        """
        attacksFirst = self.testHero.attacksFirst()
        self.assertIs(type(attacksFirst), bool)
        
    def test_heal(self):
        """
            Hero.heal() increases hero hp a 25% of origina healt
        """
        # store the initialHp
        initialHp = self.testHero.hp
        # modify hp value
        self.testHero.hp = 1.0
        # calculate the healed hp
        healedHp = self.testHero.hp + initialHp * 0.25
        self.testHero.heal()
        self.assertEqual(self.testHero.hp, healedHp)

if __name__ == '__main__':
    unittest.main()
