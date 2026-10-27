import unittest
from shop_app import login, search_product, add_to_cart, process_payment

class TestShoppingIntegration(unittest.TestCase):
    
    # Test Interface 1: Login -> Search[cite: 5]
    def test_login_to_search(self):
        auth_status = login("student", "Pass@123")
        search_result = search_product(auth_status, "laptop")
        # Should return a valid price (integer) rather than an access error
        self.assertEqual(search_result, 50000)

    # Test Interface 1: Failed Login -> Search integration[cite: 5]
    def test_failed_login_to_search(self):
        auth_status = login("wronguser", "wrongpass")
        search_result = search_product(auth_status, "laptop")
        self.assertEqual(search_result, "Error: User not logged in")

    # Test Interface 2: Search -> Cart[cite: 5]
    def test_search_to_cart(self):
        # Simulating passing price from search to cart
        price = search_product(True, "mouse")
        cart_total = add_to_cart(price, 2)
        self.assertEqual(cart_total, 1000)

    # Test Interface 3: Cart -> Payment[cite: 5]
    def test_cart_to_payment(self):
        # Simulating passing total from cart to payment
        cart_total = add_to_cart(1500, 2) # Keyboard price * 2
        payment_result = process_payment(cart_total)
        self.assertEqual(payment_result, "Payment of ₹3000 Successful")

    # Full End-to-End Integration Flow: Login -> Search -> Cart -> Payment[cite: 5]
    def test_full_end_to_end_integration(self):
        auth_status = login("student", "Pass@123")
        self.assertTrue(auth_status)
        
        price = search_product(auth_status, "laptop")
        self.assertEqual(price, 50000)
        
        cart_total = add_to_cart(price, 1)
        self.assertEqual(cart_total, 50000)
        
        payment_result = process_payment(cart_total)
        self.assertEqual(payment_result, "Payment of ₹50000 Successful")

if __name__ == "__main__":
    unittest.main()