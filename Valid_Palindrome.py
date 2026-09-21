import string

text = ":aa/"

# 1. Filter out all non-alphanumeric characters and lowercase in a single pass
clean_str = "".join(char.lower() for char in text if char.isalnum())

# 2. Compare string against its reverse
is_palindrome = clean_str == clean_str[::-1]

print(is_palindrome)