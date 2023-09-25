
# 1. In your own words, describe what a function is
"A function is a reusable piece code that performs a certain task"

# 2. What is are function parameters and arguments and describe
# the difference between the two. 
"A function parameter is a placeholder- goes in function defination."  
"A function argument is the actual data- goes in function call."

def addTwo(randomNumber):
    print(randomNumber + 2) # add 2 to the random number

addTwo(2)
addTwo(567)
# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def welcome_msg(username):
    print('welcome '+ username)


welcome_msg('Wade Briscoe')

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)


def calculate(randNumber, randomNumber2, randomNumber3):
    print(randNumber + randomNumber2 + randomNumber3)

calculate(7,362,547) #7 362 547
# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.  
def userMsg():
    nextClass = input('what is your next class.')
    print("you have " + nextClass +" after this.")

userMsg()