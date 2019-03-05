# The input funtion can be used to prompt for input and use that input in your python code. Prompt user to enter a positive number and write a loop that counts from 0 to that number.

number = input('Please enter a positive number: ')
number = int(number)

# --------------------------------------------------------------------------------- #

for number in range(number + 1):
    print(number)

# Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not
# day_of_the_week = input("Enter a day of the week: ")

if day_of_the_week == "Monday":
    print("Today is Monday")
else:
    print("Today is not Monday")

# # b. promt the user for a day of the week, print out whether the day is a weekday or a weekend

if day_of_the_week == day_of_the_week.startswith('S'):
    print("Yay! It's the weekend!")
else:
    print("It's not the weekend yet...")

# c. create variables and make up values for [ the number of hours worked in one week, the hourly rate, how much the week's paycheck will be]

number_of_hours_worked = int(input('How many hours did you work this week? '))
pay_rate = float(input('What is your hourly rate? '))

if number_of_hours_worked > 40:
  overtimeRate = 1.5 * pay_rate
  overtime = (number_of_hours_worked-40) * overtimeRate
  number_of_hours_worked = 40
else:
  overtime = 0

regular_hours = number_of_hours_worked * pay_rate

total_paycheck = regular_hours + overtime
print(f"Your total paycheck will be {total_paycheck}")


# --------------------------------------------------------------------------------- #

# 2. Loop Basics
# a. While
# Create an interager variable i with a value of 5
# Create a while loop that runs so long as i is less than 15
# Each loop iteration, output the current value of i, then increment i by one

i = 5

while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line

i = 0

while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10

i = 100

while i >= -10:
    print(i)
    i -= 5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000

i = 2

while i < 1_000_000:
    print(i)
    i **= 2

i = 100

while i >= 5:
    print(i)
    i -= 5

# b. For Loops
# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input("Please enter a number: "))

i = 1

while i <= 10:
    product = number * i
    print(f"{number} x {i} = {product}")
    i += 1

create a for loop that uses print to create the output shown below.

n = int(9)

for i in range(1,n+1):
    print(' '.join(str(i)*i))

# break and continue
# i. Promt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input.
# use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

number = input("Please enter an odd number (1 - 50): ")
while not number.isdigit() or int(number) < 1 or int(number) > 50 or int(number) % 2 ==0:
    number = input("Please enter an odd number (1 - 50): ")

number = int(number)

for n in range(50):
    if n % 2 == 0:
        continue
    if n == number:
        print("Yikes! Skipping number: " + str(number))
        continue
    else:
        print('Here is an odd number: {}'.format(n))

# d. Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

upper_bound = int(input('Please enter a number: '))
for n in range(0, upper_bound +1):
    print(n)

# e. Write a program that prompts the use for a positive interger. Next write a loop that prints out the numbers from the user entered down to 1

starting_point = int(input('Enter a starting number: '))
for n in range(starting_point, 0, -1):
    print(n)

# 3. Fizzbuzz (*** Common Interview Question***)

i = range(1, 101)

for j in i:
    if j % 3 == 0 and j % 5 == 0:
        print ("Fizz Buzz")
    elif j % 5 == 0:
        print ("Buzz")
    elif j % 3 == 0:
        print ("Fizz")
    else:
        print(j)     

# 4. Display a table of powers

upper_bound = int(input('Enter a number: '))

print('number | squared | cubed')
print('------ | ------- | -----')
for n in range(1, upper_bound + 1):
    print('{:<6} | {:<7} | {:<5}'.format(n, n ** 2, n ** 3))


# 5 .Convert given number grades into letter grades

grade = int(input("Enter a number grade: "))

if grade > 88:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 67:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

# 1. Create a list of dictionaries where each dictionary represents a book that
#    you have read. Each dictionary in the list should have the keys `title`,
#    `author`, and `genre`. Loop through the list and print out information about
#    each book.
books = [
    {
        'title': 'Data Science For Dummies',
        'author': 'Lillian Pierson',
        'genre': ['Data Science', 'Python', 'Programming']
    },
    {
        'title': 'Data Jujitsu: The Art of Turning Data into Product',
        'author': 'DJ Patil',
        'genre': ['Visualizations', 'Data Science']
    },
    {
        'title': 'Artificial Intelligence: A Modern Approach ',
        'author': 'Stuart Russell',
        'genre': ['AI', 'Machine Learning']
    },
    {
        'title': 'Deep Learning',
        'author': 'Ian Goodfellow',
        'genre': ['Deep Learning', 'Machine Learning']
    }
]

genre_to_show = input('Enter a genre: ')

for book in books:
    if genre_to_show not in book['genre']:
        continue
    print('-------------------------')
    print('- title: %s' % book['title'])
    print('- author: %s' % book['author'])
    print('- genre: %s' % book['genre'])