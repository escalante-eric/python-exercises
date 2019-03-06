# Create a file named 4.4_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# def is_two(n):
#     if n == '2':
#         return True
#     else:
#         return False

# n = input('Please enter a number: ')
# print(is_two(n))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# def is_vowel(n):
#     if n in 'aeiou':
#         return True
#     else:
#         return False

# vowel = input('Please enter a letter: ')
# print(is_vowel(vowel))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# def is_consonant(n):
#     if n in 'aeiou':
#         return False
#     else:
#         return True

# consonant = input('Please enter a letter: ')
# print(is_consonant(consonant))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# def string(word):
#     if not word.startswith('aeiou'):
#         return word.title()

# print(string('hello world'))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# def calculate_tip(tip_percentage, bill_total):
#     return (bill_total * tip_percentage) + bill_total

# print(calculate_tip(.11, 32))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# def apply_discount(original_price, discount_percentage):
#     return original_price - (original_price * discount_percentage)

# print(apply_discount(200, .15))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# def handle_commas(n):
#     return n.replace(',', '')

# print(handle_commas('1,000'))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# def get_letter_grade(n):
#     if n > 88:
#         return 'A'
#     elif n >= 80:
#         return 'B'
#     elif n >= 67:
#         return 'C'
#     elif n >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(get_letter_grade(88))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# def remove_vowels(n):
#     for i in 'aeiouAEIOU':
#         n = n.replace(i,'')
#     return n

# print(remove_vowels('Hello, World'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

# def normalize_name(n)

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# def cumsum(list):
#     total = 0                           # starting at index 0
#     cumulative_sum = []                 # make sure return value is a list
#     for value in list:
#         total += value                  # increment by each value
#         cumulative_sum.append(total)    # add the new value to the end of the list
#     return cumulative_sum               # return the cumulitive sum list

# list_of_numbers = [1, 2, 3, 4]
# print(cumsum(list_of_numbers))
