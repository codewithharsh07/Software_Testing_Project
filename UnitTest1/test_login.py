import unittest
from login_app import login

class TestLoginPage(unittest.TestCase):
    
    # Test 1: Valid inputs[cite: 1]
    def test_valid_login(self):
        result = login("student", "Pass@1234")
        self.assertEqual(result, "Login Success")

    # Test 2: Invalid inputs (wrong password)[cite: 1]
    def test_invalid_login(self):
        result = login("student", "WrongPass")
        self.assertEqual(result, "Error: Invalid Credentials")

    # Test 3: Empty fields[cite: 1]
    def test_empty_username(self):
        result = login("", "Pass@1234")
        self.assertEqual(result, "Error: Empty Field")

    # Test 4: SQL Injection attempt[cite: 1]
    def test_sql_injection(self):
        result = login("' OR '1'='1", "Pass@1234")
        self.assertEqual(result, "Error: SQL Injection Attempt")

    # Test 5: Password length[cite: 1]
    def test_short_password(self):
        result = login("student", "short")
        self.assertEqual(result, "Error: Password too short")

if __name__ == "__main__":
    unittest.main()