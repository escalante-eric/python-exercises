# Create a file named 4.7_numpy_exercises.py for this exercise.
import numpy as np

print('\n')
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
print('Negative number count: {}'.format(len(a[a < 0])))

# 2. How many positive numbers are there?
print('Positve number count: {}'.format(len(a[a > 0])))

# 3. How many even positive numbers are there?
print('Even Positive number count: {}'.format(sum(x>0 and x%2==0 for x in a)))

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
a_with_three_added = a + 3

print('Positve number count: {}'.format(sum(x > 0 for x in a_with_three_added)))

# 5. If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2

print('The New Mean is: %.2f' % np.mean(a_squared))
print('The New Standard Dev is: %.2f' % np.std(a_squared))

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
print('Centered Data: {}'.format(a - a.mean()))


# 7. Calculate the z-score for each data point. Recall that the z-score is given

print('Z-score for each data point: {}'.format((a - a.mean() / a.std())))
print('\n')

# 8. Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.

## Setup 1
aa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_aa to hold the sum of all the numbers in above list

sum_of_aa = aa.sum()
print('Sum of all the numbers: {}'.format(sum_of_aa))

# Exercise 2 - Make a variable named min_of_aa to hold the minimum of all the numbers in the above list
min_of_aa = aa.min()
print('Minimum of all numbers: {}'.format(min_of_aa))

# Exercise 3 - Make a variable named max_of_aa to hold the max number of all the numbers in the above list
max_of_aa = aa.max()
print('Maximum of all numbers: {}'.format(max_of_aa))

# Exercise 4 - Make a variable named mean_of_aa to hold the average of all the numbers in the above list
mean_of_aa = aa.mean()
print('Mean of all numbers: {}'.format(mean_of_aa))

# Exercise 5 - Make a variable named product_of_aa to hold the product of multiplying all the numbers in the above list together
product_of_aa = aa.prod()
print('Product of all numbers: {}'.format(product_of_aa))

# Exercise 6 - Make a variable named squares_of_aa. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_aa = [i**2 for i in aa]
print('Each number squared: {}'.format(squares_of_aa))

# Exercise 7 - Make a variable named odds_in_aa. It should hold only the odd numbers
odds_in_aa = (aa[aa %2==1])
print('Odd Numbers: {}'.format(odds_in_aa))

# Exercise 8 - Make a variable named evens_in_aa. It should hold only the evens.
evens_in_aa = (aa[aa %2==0])
print('Even Numbers: {}'.format(evens_in_aa))
print('\n')

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = b.sum()
print('Sum of b: {}'.format(sum_of_b))

# Exercise 2 - refactor the following to use numpy.
min_of_b = b.min()
print('Min of b: {}'.format(min_of_b))

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()
print('Max of b: {}'.format(max_of_b))

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()
print('Mean of b: {}'.format(mean_of_b))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = b.prod()
print('Product of b: {}'.format(product_of_b))

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = ([i**2 for i in b])
print('Squares of b: {}'.format(squares_of_b))

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = (aa[aa %2==1])
print('Odds in b: {}'.format(odds_in_b))

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = (b[b %2==0])
print('Even Numbers: {}'.format(evens_in_b))

# Exercise 9 - print out the shape of the array b.
print('The shape of array b: {}'.format(b.shape))

# Exercise 10 - transpose the array b.
print('The view of array with axes transposed: {}'.format(b.transpose()))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print('Reshaped b to be a single list of 6: {}'.format(b.reshape(1,6)))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print('Reshaped b to be a single list of 6: {}'.format(b.reshape(6,1)))

