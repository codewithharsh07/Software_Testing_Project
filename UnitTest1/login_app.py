def login(username, password):
    # Check for empty fields
    if username == "" or password == "":
        return "Error: Empty Field"
        
    # Check for SQL Injection attempt (looking for single quotes)
    if "'" in username or "'" in password:
        return "Error: SQL Injection Attempt"
        
    # Check password length
    if len(password) < 8:
        return "Error: Password too short"
        
    # Valid login check
    if username == "student" and password == "Pass@1234":
        return "Login Success"
        
    return "Error: Invalid Credentials"

# This section runs only when you execute the file directly
if __name__ == "__main__":
    print("--- Login Page Testing ---")
    user_input = input("Enter Username: ")
    pass_input = input("Enter Password: ")
    
    result = login(user_input, pass_input)
    print("System Output:", result)