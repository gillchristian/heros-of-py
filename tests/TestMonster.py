import unittest
import json
from units.monsters.monster import Monster

class TestMonster(unittest.TestCase):

    def setUp(self):
        with open('data/monsters.json') as data_file:
            monsters = json.loads(data_file.read())
            self.testMonster = Monster(monsters[0])

    def test_attack_equal_own_damage(self):
        """
            Monster.attack() equal to monster damage
        """
        self.assertEqual(self.testMonster.attack(), self.testMonster.damage )

    def test_receiveDamage_hp_decrease(self):
        """
            Monster.hp should decrease after receiving damage
        """
        # store the starting hp
        prev = self.testMonster.hp
        # calculate the realDamage (with armor reduction)
        realDamage = 10.0 * self.testMonster.damageMultiplier()
        # calculate the hp that should be left after attack
        hpLeft = self.testMonster.hp - realDamage
        # receive damage
        self.testMonster.receiveDamage(10.0)

        self.assertGreater(prev, self.testMonster.hp)
        self.assertLess(self.testMonster.hp, prev)
        self.assertEqual(self.testMonster.hp, hpLeft)

    def test_receiveDamage_set_dead(self):
        """
            Monster should die after receiving letal damage
        """
        self.testMonster.hp = 0
        self.testMonster.receiveDamage(10.0)
        self.assertTrue(self.testMonster.dead)

    def test_receiveDamage_receive_head_shot(self):
        """
            Monster should die on letal habilities (incomingDamage = -1.0)
        """
        self.testMonster.receiveDamage(-1.0)
        self.assertTrue(self.testMonster.dead)

    def test_receiveDamage_return_damage(self):
        """
            Monster.receiveDamage() should return the received damage
        """
        # equal to received damage when armor == 0
        self.testMonster.armor = 0
        self.assertEqual(self.testMonster.receiveDamage(10.0), 10.0)

        # less than received damage when armor > 0
        self.testMonster.armor = 5.0
        self.assertLess(self.testMonster.receiveDamage(10.0), 10.0)

        # greater than received damage when armor < 0
        self.testMonster.armor = -5.0
        self.assertGreater(self.testMonster.receiveDamage(10.0), 10.0)

        # on letal habilities, return damage received, not -1.0
        self.assertNotEqual(self.testMonster.receiveDamage(-1.0), -1.0)

    def test_damageMultiplier_armor_values(self):
        """
            Monster.damageMultiplier() should return a multiplier according to the self.armor
        """
        # equal to 1.0 when armor == 0
        self.testMonster.armor = 0
        self.assertEqual(self.testMonster.damageMultiplier(), 1.0)

        # less than 1.0 when armor > 0
        self.testMonster.armor = 5.0
        self.assertLess(self.testMonster.damageMultiplier(), 1.0)

        # greater than 1.0 when armor < 0
        self.testMonster.armor = -5.0
        self.assertGreater(self.testMonster.damageMultiplier(), 1.0)

    def test_isDead_and_die(self):
        """
            Monster.die() should set Monster.dead to True
            Monster.isDead() should be equal to Monster.dead
        """
        self.assertFalse(self.testMonster.dead)
        self.assertFalse(self.testMonster.isDead())
        self.assertEqual(self.testMonster.isDead(), self.testMonster.dead)

        self.testMonster.die()

        self.assertTrue(self.testMonster.dead)
        self.assertTrue(self.testMonster.isDead())
        self.assertEqual(self.testMonster.isDead(), self.testMonster.dead)

if __name__ == '__main__':
    unittest.main()
