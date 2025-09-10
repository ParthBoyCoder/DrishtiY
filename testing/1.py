import re

def remove_symbols(text: str) -> str:
    # keep only letters, numbers, and spaces
    return re.sub(r'[^A-Za-z0-9 ]+', '', text)

# Example usage
s = "Hello!!! My#Code$123%"
print(remove_symbols(s))  # Output: Hello MyCode123
