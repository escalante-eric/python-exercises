# Create a file named 4.8_pandas_exercises.py to do your work in for this exercise.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

# 1. Use pandas to convert the following list to a numeric series:

numeric_series = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

df_numeric_series = pd.DataFrame({'number': numeric_series})

print('\n---\n')
print(df_numeric_series)
print('\n')
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
print((df.cty > df.hwy).sum())

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
df['mileage_difference'] = df.hwy - df.cty

# On average, which manufacturer has the best miles per gallon?
print(df[['manufacturer', 'hwy', 'cty']]\
    .groupby('manufacturer')\
    .mean()\
    .sort_values(by='hwy', ascending=False)\
    .head(1))

# How many different manufacturers are there?
print('Number of different manufacturers: {}'.format(df.manufacturer.nunique()))

# How many different models are there?
print('Number of different models: {}'.format(df.model.nunique()))

# Do automatic or manual cars have better miles per gallon?
print(df[['mileage_difference', 'trans']]\
    .groupby('trans')\
    .agg([np.max]))
print('\n')
# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

df_Mammals = data('Mammals')
print('The columns in our data frame are: {}'.format(', '.join(df_Mammals.columns)))

# How many rows and columns are there?
print('Count of rows, columns: {}'.format(df_Mammals.shape))

# What are the data types?
print('Data types: {}'.format(df_Mammals.dtypes))

# What is the the weight of the fastest animal?
print(df_Mammals.nlargest(1,'speed'))

# What is the overall percentage of specials?
percent_specials = df_Mammals.specials.sum() / df_Mammals.weight.count()
print('{:.2%} are specials'.format(percent_specials))

# How many animals are hoppers that are above the median speed? What percentage is this?
print(df_Mammals.hoppers[df_Mammals.speed > df_Mammals.speed.quantile(0.5)]\
    .sum())
print(df_Mammals.hoppers[df_Mammals.speed > df_Mammals.speed.quantile(0.5)]\
    .sum() / df_Mammals.shape[0])
print('\n')

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
employees = pd.read_sql('SELECT * FROM employees', conn)
titles = pd.read_sql('SELECT * FROM titles', conn)

# Visualize the number of employees with each title.
titles.title.value_counts().plot.bar()
plt.xticks(rotation=30)
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.2)

# Visualize how frequently employees change titles.
titles.emp_no.value_counts().value_counts()

# Use the .join method to join the employees and titles data frames together
employees_with_titles = employees.join(titles, on='emp_no',     lsuffix='_emp', how='inner')
print(employees_with_titles.groupby('title')[['hire_date']]     .max())

# For each title, find the hire date of the employee that was hired most recently with that title.
print(pd.read_sql('select e.hire_date, t.title \
                from employees as e \
                join titles as t on e.emp_no = t.emp_no \
                group by t.title, e.hire_date \
                order by e.hire_date \
                limit 10', conn))

print('\n')
# 5. xplore the data from the chipotle database. Write a python script that will use this data to answer the following questions:
conn = get_connection('chipotle', user, host, password)
orders = pd.read_sql('SELECT * FROM orders', conn)
orders.item_price = orders.item_price.str.replace('$', '')\
    .astype('float')

# What is the total price for each order?
total_price = orders[['order_id', 'item_price']]\
    .groupby('order_id')\
    .sum()
print(total_price)

# What are the most popular 3 items?
popular_three = orders.item_name\
    .value_counts()\
    .head(3)
print(popular_three)

# Which item has produced the most revenue?
most_revenue = orders[['item_name', 'item_price']]\
    .groupby('item_name')\
    .sum()\
    .nlargest(1, 'item_price')
print(most_revenue)
