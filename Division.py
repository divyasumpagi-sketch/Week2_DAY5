# Handle Division by Zero
def safe_division(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
safe_division(10, 0)
