#1
def filter_positive(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positive_numbers  # Error here

print(filter_positive([-3, 5, -1, 7, 0, -2]))

#2
def sum_numbers(numbers):
    total = sum(numbers)
    if total = 0:  # Error here
        return "Zero"
    return total

print(sum_numbers([1, 2, 3, -6]))

#3
def remove_duplicates(lst):
    unique_list = list(set(lst))
    return unique_list.sort()  # Error here

print(remove_duplicates([3, 1, 2, 3, 4, 2]))

#4
def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences.keys()  # Error here

print(count_occurrences(["apple", "banana", "apple", "orange"]))

#5

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid] + numbers[mid-1] / 2)  # Error here
    return numbers[mid]

print(find_median([3, 1, 4, 2, 5]))

###########################################

#1

def reverse_string(s):
    return s.reverse()  # Error here

print(reverse_string("hello"))


#2

def capitalize_words(sentence):
    words = sentence.split()
    return words.capitalize()  # Error here

print(capitalize_words("hello world"))


#3

def is_palindrome(s):
    return s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1  # Error here]

print(is_palindrome("A man a plan a canal Panama"))


#4

def format_name(first, last):
    return f"{first.capitalize()} {last.capitalize]()"  # Error here

print(format_name("john", "doe"))


#5

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)[:-1]  # Error here

print(longest_word("The quick brown fox jumped over the lazy dog"))





