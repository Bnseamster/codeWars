import sys, unittest
sys.path.insert(0, r'C:\Users\Brand\OneDrive\Documents\CodeWars & LeetCode\CodeWars\8kyu')
from isNDivisibleByXandY import is_divisible

class TestIsNDivisible(unittest.TestCase):
    def test_is_divisible(self):

        self.assertEqual(is_divisible(15,3,5),True)
        self.assertEqual(is_divisible(21,3,7),True)
        self.assertEqual(is_divisible(85,17,5),True)
        self.assertEqual(is_divisible(3,3,3),True)
        self.assertEqual(is_divisible(3,5,15),False)
        self.assertEqual(is_divisible(40,10,3),False)
        self.assertEqual(is_divisible(3,5,6), False)


        with self.assertRaises(Exception):
            is_divisible('hi',3,3)
            is_divisible(3,'hi',3)
            is_divisible(3,3,'hi')



if __name__ == '__main__':
    unittest.main()
