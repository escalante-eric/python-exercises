# Create a file named 4.4_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
print('\n')

def is_two(n):
    '''Prints true or false depenting if the string entered is '2'
    '''
    return n == '2' or n == 2

print(is_two.__doc__)
print('is_two(2) = %s' % is_two(2))
print('is_two("2") = %s' % is_two('2'))
print('is_two(3) = %s' % is_two(3))
print('\n')

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(n):
    '''Prints true or false depenting on if the string entered is a vowel
    '''
    return n in 'aeiou'

print(is_vowel.__doc__)
print("is_vowel('a') == %s" % is_vowel('a'))
print("is_vowel('e') == %s" % is_vowel('e'))
print("is_vowel('y') == %s" % is_vowel('y'))
print('\n')

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(n):
    '''Prints true or false depenting on if the string entered is a vowel
    '''
    return not is_vowel(n)

print(is_consonant.__doc__)
print("is_consonant('a') == %s" % is_consonant('a'))
print("is_consonant('e') == %s" % is_consonant('e'))
print("is_consonant('y') == %s" % is_consonant('y'))
print('\n')

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_if_consonant(word):
    '''Prints out a string with a capitalized first char if the char is a constant
    '''
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word

print(cap_if_consonant.__doc__)
print("cap_if_consonant('codeup') == %s" % cap_if_consonant('codeup'))
print("cap_if_consonant('ada') == %s" % cap_if_consonant('ada'))
print("cap_if_consonant('Codeup') == %s" % cap_if_consonant('Codeup'))
print('\n')

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill_total):
    '''Prints out the abount to tip based on the total bill and the % of tip
    '''
    return bill_total * tip_percentage

print(calculate_tip.__doc__)
print("calculate_tip(0.2, 20) == %s" % calculate_tip(0.2, 20))
print("calculate_tip(0.15, 10) == %s" % calculate_tip(0.15, 10))
print('\n')

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    '''Prints out the new price after a discount is applied
    '''
    return original_price - (original_price * discount_percentage)

print(apply_discount.__doc__)
print("apply_discount(10, 0.2) == %s" % apply_discount(10, 0.2))
print("apply_discount(50, 0.8) == %s" % apply_discount(50, 0.8))
print('\n')

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(n):
    '''Prints out a string of numbers without the ','s
    '''
    n_without_commas = n.replace(',', '')
    return int(n_without_commas)

print(handle_commas.__doc__)
print("handle_commas('1,234') == %s" % handle_commas('1,234'))
print("handle_commas('1,234,567') == %s" % handle_commas('1,234,567'))
print('\n')

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(n):
    '''Prints out the letter grade associated with the number grade
    '''
    if n > 88:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 67:
        return 'C'
    elif n >= 60:
        return 'D'
    else:
        return 'F'

print(get_letter_grade.__doc__)
print("get_letter_grade(84) == %s" % get_letter_grade(84))
print("get_letter_grade(12) == %s" % get_letter_grade(12))
print('\n')

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(n):
    '''Prints out a string with vowels removed
    '''
    return ''.join([letter for letter in n if is_consonant(letter)]).lower()

print(remove_vowels.__doc__)
print("remove_vowels('Hello, World') == %s" % (remove_vowels('Hello, World')))
print("remove_vowels('Whatsup ada') == %s" % (remove_vowels('Whatsup ada')))
print('\n')

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores



LETTERS = ' _abcdefghijklmnopqrstuvwxyz0123456789'

def normalize_name(n):
    '''Prints a valid python identifier once string n is entered
    '''
    n = n.lower()
    valid_char = []
    for char in n:
        if char in LETTERS:
            valid_char.append(char)
    return ''.join(valid_char).strip().replace(' ', '_')

print(normalize_name.__doc__)
print("normalize_name('Name') == %s" % normalize_name('Name'))
print("normalize_name('First Name') == %s" % normalize_name('First Name'))
print('\n')

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumsum(list):
    '''Prints the list that is the cumulative sum of numbers in the accepted list
    '''

    total = 0                           # starting at index 0
    cumulative_sum = []                 # make sure return values are in a list
    for value in list:
        total += value                  # increment by each value
        cumulative_sum.append(total)    # add the new value to the end of the list
    return cumulative_sum               # return the cumulitive sum list


print(cumsum.__doc__)
print("cumsum([1, 2, 3]) == %s" % cumsum([1, 2, 3]))
print("cumsum([1, 1, 1]) == %s" % cumsum([1, 1, 1]))
print('\n')


