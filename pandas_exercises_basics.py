### Basics
# 1. Import pandas and numpy
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# 2. Use the code below to generate a data frame for students
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
print(df.sample(5))

# 8. Create a new data frame that has only columns for favorite number and name, and only includes 7 rows.
print(df[['favorite_number','student_name']].sample(7))

# 9. Create a new column for the ratio of shoe size to the favorite number. Name this ss_to_fn
df['ss_to_fn'] = df.shoe_sizes / df.favorite_number

# 10. Create a new column that contains the z-score for the shoe size.
df['z-score_shoe_sizes'] = (df.shoe_sizes - df.shoe_sizes.mean() / df.shoe_sizes.std())

# 11. Transform the side_of_the_classroom columns such that the values are either R or L.
df['side_of_classroom'] = df.side_of_classroom.str[0].str.upper()

# 12. Find the names of all the students that have a shoe size greater than the 3rd quartile of shoe sizes (You can use the .quantile method on a series for this)
df[df.shoe_sizes < df.shoe_sizes.quantile(0.25)]

# 13. Find the names of all the students that have a shoe size less than the 1st quartile of shoe sizes
df[df.shoe_sizes < df.shoe_sizes.quantile(0.75)]

### Aggregation & Plotting
# 1. Calculate the mean, median, min, and max for the shoe sizes and favorite numbers
for col in ['shoe_sizes', 'favorite_number']:
    print('-- {} class'.format(col.capitalize()))
    print('  - Mean:{:.2f}'.format(df[col].mean()))
    print('  - Min: {:.2f}'.format(df[col].min()))
    print('  - Max: {:.2f}'.format(df[col].max()))

# 2. Sort the data frame by the students shoe size
df.sort_values(by='shoe_sizes')

# 3. Sort the data frame by the side of the classroom, then by their student number
df.sort_values(by='shoe_sizes').sort_values(by='student_number')

# 4. Find the number of students on each side of the classroom
print(df[['student_name','side_of_classroom']].groupby('side_of_classroom').count())

# 5. Find the average shoe size for each side of the classroom
print(df[['shoe_sizes', 'side_of_classroom']].groupby('side_of_classroom').agg([np.mean]))

# 6. Find the maximum favorite number for each side of the classroom
print(df[['favorite_number', 'side_of_classroom']].groupby('side_of_classroom').agg([np.max]))

# 7. Create a pie chart that visualizes the number of students on each side of the classroom.


# 8. Create a histogram of the shoe sizes in the classroom
df.shoe_sizes.plot.hist()

# 9. Create a histogram of the favorite numbers in the classroom
df.favorite_number.plot.hist()

# 10. Create a scatter plot of shoe size vs favorite number
df.plot.scatter(x='shoe_sizes', y='favorite_number')

### Reading & Writing Data
# 1. Save the students data to a csv file.

students = '''Sally; 
              Jane; 
              Suzie; 
              Billy; 
              Ada; 
              John; 
              Thomas;
              Marie; 
              Albert; 
              Richard; 
              Isaac; 
              Alan'''.strip()

with open('students.csv', 'w') as f:
    f.write(students)

# 2. Read the data from the csv file back into pandas. What do you notice?
print(pd.read_csv('students.csv', header=None, sep=';'))

# 3. Create a data frame based on the profiles.json file. Explore this data frame's structure
import json

with open('profiles.json') as json_data:
    print(pd.read_json('profiles.json'))


from os import remove as rm

for file in ('students.csv', 'profiles.json'):
    try:
        rm(file)
    except FileNotFoundError:
        pass

# 4. Write the code necessary to create a data frame based on the results of a SQL query to the numbers database.
from env import user, host, password

def get_connection(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)

conn = get_connection('ada_students', user, host, password)

df_sql = pd.read_sql('select sg.group_id, s.first_name \
                        from student_groups as sg \
                        join students as s \
                        on sg.student_id = s.student_id \
                        order by sg.group_id', conn)

print(df_sql)

