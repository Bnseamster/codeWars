import sys, unittest
sys.path.insert(0, r'C:\Users\Brand\OneDrive\Documents\CodeWars & LeetCode\CodeWars\8kyu')
from centuryFromYear import century



class TestCentury(unittest.TestCase):
    

    def test_century(self):
        self.assertEqual(century(1783), 18)
        self.assertEqual(century(1), 1)
        self.assertEqual(century(2000), 20)

    


if __name__ == "__main__":
    unittest.main()