import Character
import unittest

class TestCharCreation(unittest.TestCase):
    def test_strength(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.strength,12)

    def test_MP(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.MPmax,12)

    def test_mana(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.mana,8)

    def test_losthp(self):
        temp=Character.character("testchar.aks16")
        temp.vitality=temp.vitality-2
        self.assertEqual(temp.vitality,43)

if __name__ == '__main__':
    unittest.main()
