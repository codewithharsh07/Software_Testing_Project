import unittest
from age_app import validate_age

class TestAgeValidation(unittest.TestCase):
    
    # --- Boundary Value Analysis (BVA) Test Cases ---
    
    def test_lower_boundary_invalid(self):
        # Age 17 is just below the lower limit (Invalid)[cite: 2]
        result = validate_age(17)
        self.assertEqual(result, "Error: Age must be between 18 and 60")

    def test_lower_boundary_exact(self):
        # Age 18 is the exact lower limit (Valid)[cite: 2]
        result = validate_age(18)
        self.assertEqual(result, "Valid Age: Accepted")

    def test_upper_boundary_exact(self):
        # Age 60 is the exact upper limit (Valid)[cite: 2]
        result = validate_age(60)
        self.assertEqual(result, "Valid Age: Accepted")

    def test_upper_boundary_invalid(self):
        # Age 61 is just above the upper limit (Invalid)[cite: 2]
        result = validate_age(61)
        self.assertEqual(result, "Error: Age must be between 18 and 60")

    # --- Equivalence Partitioning (EP) Test Cases ---
    
    def test_valid_partition(self):
        # Age 35 is a random valid number between 18 and 60[cite: 2]
        result = validate_age(35)
        self.assertEqual(result, "Valid Age: Accepted")

    def test_invalid_partition_low(self):
        # Age 5 is a random invalid number below 18[cite: 2]
        result = validate_age(5)
        self.assertEqual(result, "Error: Age must be between 18 and 60")
        
    def test_invalid_partition_high(self):
        # Age 75 is a random invalid number above 60[cite: 2]
        result = validate_age(75)
        self.assertEqual(result, "Error: Age must be between 18 and 60")

    def test_invalid_data_type(self):
        # Testing what happens if someone types text instead of numbers
        result = validate_age("abc")
        self.assertEqual(result, "Error: Please enter a valid number")

if __name__ == "__main__":
    unittest.main()