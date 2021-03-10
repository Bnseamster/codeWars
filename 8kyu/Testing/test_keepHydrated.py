import unittest,sys
sys.path.insert(0,r'C:\Users\Brand\OneDrive\Documents\CodeWars & LeetCode\CodeWars\8kyu')
from keepHydrated import litres



class TestKeepHydrated(unittest.TestCase):
    
    #individual test counts as one test
    def testLitres(self):  
        
        self.assertEqual(litres(5),2)
        self.assertEqual(litres(15), 7)
        self.assertEqual(litres(3), 1)
        self.assertEqual(litres(0), 0)
        self.assertEqual(litres(.7), 0)
        self.assertEqual(litres(6.3), 3)
        self.assertEqual(litres(12.582395), 6)
        #testing invalid inputs
        with self.assertRaises(Exception):
            litres('hello')
            litres('2')
        
        with self.assertRaises(Exception):
            
            litres(-2)
            litres(-60)
            litres(-5.3)





if __name__ == '__main__':
    unittest.main()