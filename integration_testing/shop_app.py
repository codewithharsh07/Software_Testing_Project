# Module 1: Login
def login(username, password):
    if username == "student" and password == "Pass@123":
        return True
    return False

# Module 2: Product Search[cite: 5]
def search_product(is_logged_in, item_name):
    if not is_logged_in:
        return "Error: User not logged in"
    
    catalog = {"laptop": 50000, "mouse": 500, "keyboard": 1500}
    if item_name.lower() in catalog:
        return catalog[item_name]
    return "Error: Product not found"

# Module 3: Cart[cite: 5]
def add_to_cart(item_price, quantity):
    if type(item_price) is not int or item_price <= 0:
        return "Error: Invalid price passed to cart"
    if quantity <= 0:
        return "Error: Quantity must be at least 1"
    
    return item_price * quantity

# Module 4: Payment[cite: 5]
def process_payment(total_amount):
    if type(total_amount) is not int or total_amount <= 0:
        return "Payment Failed: Invalid amount"
    
    return f"Payment of ₹{total_amount} Successful"

# Interactive section to test manually
if __name__ == "__main__":
    print("--- Online Shopping System ---")
    
    # 1. Login
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")
    auth_status = login(user, pwd)
    print(f"Login Status: {auth_status}")
    
    if auth_status:
        # 2. Search
        item = input("Enter product to search (laptop/mouse/keyboard): ")
        price = search_product(auth_status, item)
        print(f"Product Price: ₹{price}")
        
        if type(price) is int:
            # 3. Cart
            qty = int(input("Enter quantity: "))
            cart_total = add_to_cart(price, qty)
            print(f"Cart Total: ₹{cart_total}")
            
            # 4. Payment
            payment_status = process_payment(cart_total)
            print(f"System Output: {payment_status}")