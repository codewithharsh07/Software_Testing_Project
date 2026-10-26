def evaluate_marks(marks):
    # Check if input is a valid number
    try:
        marks = float(marks)
    except ValueError:
        return "Error: Invalid Input"

    # Core logic to evaluate pass or fail
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

# Interactive section to test manually
if __name__ == "__main__":
    print("--- Marks Evaluation System ---")
    student_marks = input("Enter marks: ")
    
    result = evaluate_marks(student_marks)
    print("System Output:", result)