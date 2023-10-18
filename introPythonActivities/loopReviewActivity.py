













# Write a loop that will work for these three scenarios

# Passcode Loop - write a program that will check
# if a passcode is correct. While the passcode is not correct;
# Ask the user to try again. User get 4 attempts

def passcode_attempt_logic():
    passcode = 1234
    passcodeAttempt_Count =0

    while passcodeAttempt_Count < 4:
        passcode_Attempt = int(input('please enter the passcode:'))
        if passcode_Attempt != passcode:
            print('Incorrect passcode. Try again.')
        else:
            print('correct! you may enter')
            break
    passcodeAttempt_Count +=1

passcode_attempt_logic()

# Printer Loop


# Stop Light Loop

