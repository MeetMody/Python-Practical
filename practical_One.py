### Question 1: **Reverse Words in a String**

# Write a function, `reverse_words(s: str) -> str`, that takes a string of words separated by spaces
# and returns the string with the words in reverse order, but keeps the order of the letters within
# each word.

# **Requirements:**

# - Ensure that multiple spaces between words are reduced to a single space in the final output.
# - If the input is an empty string, return an empty string.


def reverse_words():
    s = input("Enter a string :")
    words = s.split()
    reversed_words = words[::-1]
    join_words = ' '.join(reversed_words)
    return join_words

print(reverse_words())
