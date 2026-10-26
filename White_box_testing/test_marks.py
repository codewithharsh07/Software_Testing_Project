import unittest
from marks_app import evaluate_marks

class TestMarksEvaluation(unittest.TestCase):
    
    # Path 1 Coverage: Marks are >= 40 (True branch)[cite: 3]
    def test_path1_pass_condition(self):
        result = evaluate_marks(45)
        self.assertEqual(result, "Pass")

    # Path 1 Coverage: Exact boundary condition (True branch)[cite: 3]
    def test_path1_exact_boundary(self):
        result = evaluate_marks(40)
        self.assertEqual(result, "Pass")

    # Path 2 Coverage: Marks are < 40 (False branch)[cite: 3]
    def test_path2_fail_condition(self):
        result = evaluate_marks(35)
        self.assertEqual(result, "Fail")
        
    # Additional check for invalid data input
    def test_invalid_input(self):
        result = evaluate_marks("abc")
        self.assertEqual(result, "Error: Invalid Input")

if __name__ == "__main__":
    unittest.main()