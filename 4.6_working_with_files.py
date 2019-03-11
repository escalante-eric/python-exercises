`# Read the contents of your last exercise file into a variable.
# Print out every line in the file

# with open('4.5_import_exercises.py') as f:
#     file_contents = f.read()
#     print(file_contents)

# Print out every line in the file, but add a line numbers
# data = []
# with open('4.5_file.txt', 'a+') as n_file:
#     for num,line in enumerate(n_file):
#             print(num,line)

#Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 3 things that you need to buy from the grocery store.

grocery_list = ['chicken burger', 'cheese', 'organs' ]

# Create a function named make_grocery_list. When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.

with open('my_grocery_list.txt', 'w') as wf:
    for groceries in grocery_list:
        print(groceries, file=wf)

# Create a function named show_grocery_list. When run, it should show each item on the grocery list.

with open('my_grocery_list.txt', 'r') as rf:
    file_contents = rf.read()
    print("Grocery List:\n" + file_contents)

# Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.

def buy_item():
    with open('my_grocery_list.txt', 'a+') as f:
        f.write(test)
