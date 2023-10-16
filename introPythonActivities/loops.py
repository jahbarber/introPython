# while loop
i = 1 # iterator
while i < 6: #condition/ scenarion we want to check for
    print(i) # instruction on what to do next
    i += 1 # increment - the number of times we want to do it.


# conditional statement
def password_code():
    user_password_attempt= input("please enter a password")
    actual_password='blch'
    i = 0
    while i < 3:
        if user_password_attempt == actual_password:
            print('password correct. Please enter.')
            break
        else:
            print('invalid password, try again')
            i += 1

password_code()