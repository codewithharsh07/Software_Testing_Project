import unittest
from factorial_app import calc_fact

class TestFactorial(unittest.TestCase):
    
    def test_all_factorial_cases(self):
        # 1. Positive number[cite: 4]
        self.assertEqual(calc_fact(5), 120)
        
        # 2. Zero[cite: 4]
        self.assertEqual(calc_fact(0), 1)
        
        # 3. Negative number[cite: 4]
        self.assertEqual(calc_fact(-5), "Error: Negative")
        
        # 4. Large input[cite: 4] (10! = 3,628,800)
        self.assertEqual(calc_fact(10), 3628800)

if __name__ == "__main__":
    unittest.main()