# Create a file named 4.8_pandas_exercises.py to do your work in for this exercise.
import numpy as np
import pandas as pd

# 1. Use pandas to convert the following list to a numeric series:

numeric_series = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

df_numeric_series = pd.DataFrame({'number': numeric_series})
print('\n---\n')
print(df_numeric_series)

# 2. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

from pydataset import data

df = data('mpg') # load the dataset and store it in a variable
print('\n---\n')

# How many rows and columns are there?
print('Count of rows, columns: {}'.format(df.shape))

# What are the data types?
print('The columns in our data frame are: {}'.format(', '.join(df.columns)))
print('Data types: {}'.format(df.dtypes))

# Do any cars have better city mileage than highway mileage?
print('Median city mileage: {:.1f}'.format(df['cty'].mean()))
print('Median highway mileage: {:.1f}'.format(df['hwy'].mean()))

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
df['mileage_difference'] = df.cty - df.hwy

# On average, which manufacturer has the best miles per gallon?
print(df[['manufacturer', 'mileage_difference']].groupby('mileage_difference').agg([np.min]).head(1))

# How many different manufacturers are there?
print(df['manufacturer'].value_counts())

# How many different models are there?
print(df[['model','manufacturer']].groupby('manufacturer').count())

# Do automatic or manual cars have better miles per gallon?
print(df[['mileage_difference', 'trans']].groupby('trans').agg([np.max]))

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

df_Mammals = data('Mammals')
print('The columns in our data frame are: {}'.format(', '.join(df_Mammals.columns)))

# How many rows and columns are there?
print('Count of rows, columns: {}'.format(df_Mammals.shape))

# What are the data types?
print('Data types: {}'.format(df_Mammals.dtypes))

# What is the the weight of the fastest animal?
print(df_Mammals[['weight', 'speed']].groupby('speed').agg([np.max]).head(1))

# What is the overal percentage of specials?
print('Percentage of specials: {:.1f}'.format(df_Mammals['specials'].mean()))

# How many animals are hoppers that are above the median speed? What percentage is this?
print(df_Mammals[df_Mammals.hoppers < df_Mammals.speed.quantile(0.5)].count())

# 4. Getting data from SQL databases
from env import user, host, password

# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson. 
def get_connection(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)

# Use your function to obtain a connection to the employees database.
conn = get_connection('employees', user, host, password)

# Read the employees and titles tables into two separate data frames
print(pd.read_sql('select * from employees limit 5', conn))
print(pd.read_sql('select * from titles limit 5', conn))

# Visualize the number of employees with each title.
# Visualize how frequently employees change titles.

# Use the .join method to join the employees and titles data frames together
print(pd.read_sql('select e.hire_date, t.title from employees as e join titles as t on e.emp_no = t.emp_no limit 5', conn))

# For each title, find the hire date of the employee that was hired most recently with that title.
print(pd.read_sql('select e.hire_date, t.title \
                from employees as e \
                join titles as t on e.emp_no = t.emp_no \
                group by t.title, e.hire_date \
                order by e.hire_date \
                limit 10', conn))
            
# 5. xplore the data from the chipotle database. Write a python script that will use this data to answer the following questions:
conn_c = get_connection('chipole', user, host, password)

# What is the total price for each order?
# What are the most popular 3 items?
# Which item has produced the most revenue?
