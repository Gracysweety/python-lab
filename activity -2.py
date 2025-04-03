#1.A Python function is_palindrome(s) that checks if a string is a palindrome:

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Test cases
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("racecar"))  # Output: True

#2.A Python function find_largest(lst) that returns the largest number in a list:
def find_largest(lst):
    # Use the max() function to find and return the largest number
    return max(lst)

# Test case
numbers = [10, 20, 5, 8, 25, 3]
print(find_largest(numbers))  # Output: 25

#3.A Python function count_vowels(s) that counts the number of vowels in a given string:
def count_vowels(s):
    # Define the vowels
    vowels = "aeiouAEIOU"
    # Count vowels in the string
    count = sum(1 for char in s if char in vowels)
    return count

# Test cases
print(count_vowels("Hello World"))  # Output: 3
print(count_vowels("Python"))       # Output: 1
print(count_vowels("Beautiful Day")) # Output: 6



