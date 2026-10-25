def validate_age(age):
    # Check if the input is a valid number
    try:
        age = int(age)
    except ValueError:
        return "Error: Please enter a valid number"
        
    # Check the age range criteria (18 to 60)
    if 18 <= age <= 60:
        return "Valid Age: Accepted"
    else:
        return "Error: Age must be between 18 and 60"

# Interactive section to test manually
if __name__ == "__main__":
    print("--- Age Validation System ---")
    user_age = input("Enter your age: ")
    
    result = validate_age(user_age)
    print("System Output:", result)