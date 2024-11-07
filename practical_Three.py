### Question 3: **Group Anagrams**

# Write a function, `group_anagrams(words: List[str]) -> List[List[str]]`, that takes a list of 
# strings and groups anagrams together. Anagrams are words that contain the same letters in any order.

# **Requirements:**

# - Each group of anagrams should appear as a separate list within the main list.
# - The order of the groups in the output does not matter

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = sorted(word)
        join_word = ' '.join(sorted_word)
    
        if join_word in anagram_dict:
            anagram_dict[join_word].append(word)
        else:
            anagram_dict[join_word] = [word]
    return list(anagram_dict.values())
 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))