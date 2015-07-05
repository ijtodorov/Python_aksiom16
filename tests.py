import Character
import unittest

class TestCharCreation(unittest.TestCase):
    def test_strength(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.strength,12)
        self.assertEqual(temp.dexterity,10)

if __name__ == '__main__':
    unittest.main()
