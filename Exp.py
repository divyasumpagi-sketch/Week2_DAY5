# Another Custom Exception Example
class AgeTooLowError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is too low. Must be at least 18.")

def validate_age(age):
    if age < 18:
        raise AgeTooLowError(age)
    print("Age is valid.")

# Example usage
try:
    validate_age(15)
except AgeTooLowError as e:
    print(e)
