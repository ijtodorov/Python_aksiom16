import Character
import unittest

class TestCharCreation(unittest.TestCase):
    def test_strength(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.strength,12)

    def test_MP(self):
        temp=Character.character("testchar.aks16")
        self.assertEqual(temp.MPmax,12)

if __name__ == '__main__':
    unittest.main()
