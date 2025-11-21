# nested lists, calculate sum of all values

# 1. recursively

def nested_sum(nested_list):
    if not nested_list:
        return 0
    if type(nested_list[0]) == int:
        return nested_list[0] + nested_sum(nested_list[1:])
    elif type(nested_list[0]) == list:
        return nested_sum(nested_list[0]) + nested_sum(nested_list[1:])
    
# print(nested_sum([1,2,[3,4],5,[6,[7,8]]]))

# 2. iteratively

def iter_nest(nested_list):
    total = 0
    for item in nested_list:
        if type(item) == int:
            total += item
        elif type(item) == list:
            total += iter_nest(item)
    return total

# print(iter_nest([1,2,[3,4],5,[6,[7,8]]]))

# count number of vowels in string (iteratively)

def count_vowels(words):
    dc = {}
    for char in words:
        char = char.lower()
        if char in "aeiou":
            dc[char] = dc.get(char, 0) + 1
    return dc

# print(count_vowels("Hello world"))

# count number of vowels in string (recursively)

def cv_rec(text):
    vowel_count = {}
    if not text:
        return {}
    char = text[-1].lower()
    if char in "aeiou":
        vowel_count[char] = vowel_count.get(char, 0)

# ts sucks, don't do it, just follow the example

def new_count_vowels(text):
    if len(text) == 0:
        return {}
    letter = text[-1].lower()
    counts = new_count_vowels(text[:-1])
    if letter in "aeiou":
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts

# sorted list (recursive)

def is_sorted(numbers):
    if len(numbers) <= 1:
        return True
    if numbers[0] <= numbers[1]:
        return is_sorted(numbers[1:])
    else:
        return False
    
# print(is_sorted([5,5,5,5]))

'''
M7 Programing Questions
'''

# remove 4 function

def remove_four(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        if "4" in str(numbers[i]):
            new_numbers.append("replaced")
        else:
            new_numbers.append(numbers[i])
    return new_numbers

# print(remove_four([1,2,45,54,99]))

# unique number across 2D matrix

def find_unique(nums):
    if not nums:
        return {}
    unique_nums = set()
    memory = []

    for sublist in nums:
        for val in sublist:
            if val in unique_nums:
                unique_nums.remove(val)
            else:
                if not val in memory: 
                    unique_nums.add(val)
                    memory.append(val)


    
    return unique_nums

print(find_unique([[10, 20], [30, 40, 50], [30, 40, 50, 60], [100]]))