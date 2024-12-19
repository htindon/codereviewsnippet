def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if string is equal to its reverse

# Example usage
word = "A man a plan a canal Panama"
print(is_palindrome(word))  # Expected Output: True
