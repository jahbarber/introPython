# read and review the following pages on Python lists. Use these to help you solve
# the questions. 

linkOne= 'https://www.w3schools.com/python/python_lists.asp'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.  

def Favorite_videogames():

    jahmere_Favorite_Videogames = input('What are your favorite games?')
    if jahmere_Favorite_Videogames == 'Blackops2, CallofdutyGhost, GTA5, Fc24, and Minecraft':
        print('These are Jahmere favorite games.')
    else:
        print('These are not Jahmere favorite games.')

Favorite_videogames()


# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3

zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']
    
print(zoo_animals[3])

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']

print(sports_on_tv[1])

# find and print index 0
random_numbers = [10,100,12123, 1394, 1]

print(random_numbers[0])

# 3. Create a program that will only print out the odd numbers in this list. 

# HINT- part of solving this is that you will need to use the range() function. 


number_list= [1,2,3,4,5,6,7,8,9,10]

print(range(1,2,3,4,5,6,7,8,9,10))

# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

shopping_cart = ['notebook', 'pens','tape','mousepad']


