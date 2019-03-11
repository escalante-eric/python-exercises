# Create a file named 4.5_import_exercises.py to do your work in.

# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# import the module and refer to the function with the . syntax
import function_exercises
# use from to import the function directly
from function_exercises import is_two
# use from and give the function a different name
from function_exercises import is_two as two

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

import itertools as it
import json


combination_var = list(it.product('abc', '123'))
print("Different way you can combine letters and numbers: {}".format(combination_var))

# 2. How many different ways can you combine two of the letters from "abcd"?

combination_letters = list(it.combinations('abcd', 2))
print("Different ways you can combine two letters: {}".format(combination_letters))
print("\n")

# Save this file as loaded_json.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

json_profiles = json.load(open('profiles.json'))

# Total number of users
print("Total number of users: {}".format(len(json_profiles)))

# Number of active users
active_users = [user for user in json_profiles if user['isActive']]
print("Number of active users: {}".format(len(active_users)))


# Number of inactive users
print("Number of inactive users: {}".format(len(json_profiles) - len(active_users)))


# Grand total of balances for all users
total_balances = sum([float(profile['balance'].replace('$',"").replace(',','')) for profile in json_profiles])
print ("Grand total of balance for all users: ${}".format(total_balances))

# Average balance per user
average_balances = [profile['balance'] for profile in json_profiles]
print("Average balace per user: ${}".format(round(total_balances/len(average_balances), 2)))

# User with the lowest balance
total_balances = [profile['balance'] for profile in json_profiles]
print("Lowest user balance {}".format(min(total_balances)))

# User with the highest balance
total_balances = [profile['balance'] for profile in json_profiles]
print("Highest user balance {}".format(max(total_balances)))

# Most common favorite fruit
favorite_fruit = [profile['favoriteFruit'] for profile in json_profiles]
count = {}
for fruit in favorite_fruit:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

print("Most common favorite fruit: {}".format(max(count)))

# Least most common favorite fruit
print("Least common favorite fruit: {}".format(min(count)))
print('\n')

# Total number of unread messages for all users 
print('--- Total number of unread messages for all users ---')
def extract_n_unread_messages(greeting: str):
    start = 'You have '
    stop = ' unread messages.'
    start_index = greeting.index(start) + len(start)
    stop_index = greeting.index(stop)
    return int(greeting[start_index:stop_index])

greetings = [user['greeting'] for user in profiles]
unread_messages = [extract_n_unread_messages(greeting) for greeting in greetings]
print(sum(unread_messages))