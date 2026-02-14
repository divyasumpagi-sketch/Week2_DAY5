# Custom Exception Example
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number not allowed: {value}")

def check_positive(num):
    if num < 0:
        raise NegativeNumberError(num)
    return num

# Example usage
try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)
