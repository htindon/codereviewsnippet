def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    left, right = 0, len(s) - 1  # Set up pointers at the start and end of the string

    while left < right:
        if s[left] != s[right]:
            return False  # If characters don't match, it's not a palindrome
        left += 1  # Move left pointer towards the middle
        right -= 1  # Move right pointer towards the middle
    
    return True  # If no mismatches were found, it's a palindrome

# Example usage
word = "A man a plan a canal Panama"
print(is_palindrome(word))  # Expected Output: True
