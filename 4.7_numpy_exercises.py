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