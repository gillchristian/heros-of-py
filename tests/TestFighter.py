import unittest
import json
from units.heros.fighter import Fighter

class TestFighter(unittest.TestCase):

    def setUp(self):
        with open('data/heros.json') as data_file:
            heros = json.loads(data_file.read())
        self.testFighter = Fighter(heros[1])

    def test_attack_increases_over_turn(self):
        """
            Fighter.attack() increases over turns
        """
        # Fighter.attack() == Fighter.damage on turn 0
        firstTurnDamage = self.testFighter.attack(0)
        self.assertEqual(firstTurnDamage, self.testFighter.damage )

        prviousTurn = firstTurnDamage
        for turn in range(1,2):
            thisTurnDamage = self.testFighter.attack(turn)
            # subsecuent turns damage should be gratear each time
            self.assertGreater(thisTurnDamage, prviousTurn)
            # hero damage should not be modified
            self.assertNotEqual(thisTurnDamage, self.testFighter.damage)
            prviousTurn = thisTurnDamage
        # turn 0 should always return starting damage
        self.assertEqual(self.testFighter.attack(0), self.testFighter.damage)

if __name__ == '__main__':
    unittest.main()
