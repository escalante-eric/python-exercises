## List Comprehension Exercises
# Use the code below to answer all of the exercises:

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
print('\n')

# 1. Rewrite the above example code below using a list comprehension. Make a variable named uppercased_fruits to hold the output of the list comprehension. 
print([x.upper() for x in fruits])

# 2. Create a variable named capitalized_fruits and use a list comprehension to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [x.title() for x in fruits]
print(capitalized_fruits)

# 3. Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# 4. Make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi']

# 5. Make a list that contains each fruit with more than 5 characters
print([fruit for fruit in fruits if len(fruit) > 5])

# 6. Make a list that contains each fruit with exactly 5 characters
print([fruit for fruit in fruits if len(fruit) == 5])

# 7. Make a list that contains fruits that have less than 5 characters
print([fruit for fruit in fruits if len(fruit) < 5])

# 8. Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


# 9. Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# 10. Make a variable named even_numbers that holds only the even numbers

# 11. Make a variable named odd_numbers that holds only the odd numbers

# 12. Make a variable named positive_numbers that holds only the positive numbers

# 13. Make a variable named negative_numbers that holds only the negative numbers

# 14. Use a list comprehension with a conditional in order to produce a list of numbers with 2 or more numerals

# 15. Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# 16. Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# 17. Make a variable named primes that is a list containing the prime numbers in the numbers list.