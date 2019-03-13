## 1. Import pandas and numpy
import numpy as np
import pandas as pd

## 2. Use the code below to generate a data frame for students
# Your data frame should include the student number, student name, shoe_size, and favorite number.
# Store your data frame in a variable named students

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

df = pd.DataFrame({'student_name': students,
                   'student_number': student_number,
                   'shoe_sizes': shoe_sizes,
                   'side_of_classroom': side_of_classroom,
                   'favorite_number': favorite_number})

# 3. Print out the shape of the data frame.
print('The shape of the data frame: {}'.format(df.shape))

# 4. Print out the names of the columns in the data frame.
print('The columns in our data frame are: {}'.format(', '.join(df.columns)))

# 5. Rename 2 of the columns in your data frame.
print(df.rename(columns={'student_number': 'student_id', 'shoe_sizes': 'shoe_size'}))

# 6. Create a new data frame based on the one you have. The new data frame should only have columns for shoe size and side of the classroom.
print(df[['shoe_sizes','side_of_classroom']])

# 7. Create a new data frame that has all of the columns, but only 5 rows.
print(df.head())

# 8. Create a new data frame that has only columns for favorite number and name, and only includes 7 rows.
print(df[['favorite_number','student_name']].head(7))

# 9. Create a new column for the ratio of shoe size to the favorite number. Name this ss_to_fn
df['ss_to_fn'] = df.shoe_sizes / df.favorite_number

# 10. Create a new column that contains the z-score for the shoe size.
df['z-score_shoe_sizes'] = (df.shoe_sizes - df.shoe_sizes.mean() / df.shoe_sizes.std())

# 11. Transform the side_of_the_classroom columns such that the values are either R or L.
df['side_of_classroom'] = df.side_of_classroom.apply(lambda side: 'R' if side == 'right' else 'L')

# 12. Find the names of all the students that have a shoe size greater than the 3rd quartile of shoe sizes (You can use the .quantile method on a series for this)


# 13. Find the names of all the students that have a shoe size less than the 1st quartile of shoe sizes

