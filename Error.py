# Handle File Errors
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read file '{filename}'.")

# Example usage
read_file("non_existent_file.txt")
