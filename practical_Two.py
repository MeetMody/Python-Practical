### Question 2: **Find the Missing Number in a List**

# Write a function, `find_missing_number(nums: List[int]) -> int`, that takes a list of consecutive 
# integers starting from 1 with one number missing. The function should return the missing number.

# **Requirements:**

# - The list will always have at least one number missing, and the numbers will always start from 1.
# - The list may not necessarily be sorted.

def find_missing_number(num_list, start, end):
    if start > end:
        return []
    if start not in num_list:
        return [start] + find_missing_number(num_list, start + 1, end)
    return find_missing_number(num_list, start + 1, end)

num_list = [ 1,2, 4, 6, 7, 9, 10]
start = num_list[0]
end = num_list[-1]
print(start, end)
print(find_missing_number(num_list, start, end))
