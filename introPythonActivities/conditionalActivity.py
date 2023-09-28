# 1. What is the difference between
# a parameter and an argument in a python function

"An argument is the data inside the round brackets and a parameter is the round brackets"

"parameter is a place holder."
"argument is the actual data."

"parameter is variable listed inside of function defination."
"argument is assigned to the function when its call."

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

"A conditional statement is an if or else statement which is when somebody does a specific function that is in the instructions do this or do not do anything"
"if money is taken out of an atm-give them physical money."
"else-don't give them money."

"executes a block of code if a specific condition is met."

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )
amount_of_money = 5.00
amount_of_money_for_candybar = 3.00
if amount_of_money > amount_of_money_for_candybar:
    print('you have enough for candybar, congrats.')
else: 
    print('sorry, you do not have enough money')



# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def put_food_in_refridgerator(fooood_in_refridgerator):
    if fooood_in_refridgerator==True:
        print('time to cook.')
    else:
        print('time to shop.')

put_food_in_refridgerator(False)

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

#keyword = parameter, integer, function, print, conditional statement, inventory,
#comparison using more than

def cereal_inventory(cereal):
    current_cereal_inventory= 10
    if cereal >= current_cereal_inventory:
        print("Inventory is full.")
    else:
        print("need to order more cereal.")

cereal_inventory(10)