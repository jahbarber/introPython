# Create while loops for the following conditions

# 1. Create a security camera program that uses a while loop to detect if there is an
# object in site. 

def security_camera_people():
    people_On_Camera = 0
    while people_On_Camera < 1 :
        
   
        people_On_Camera +=1
    if people_On_Camera>=1:
        print('Alert, people on camera!')
security_camera_people()




# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 

Document_number = 1
copies_Of_Document= 3

while copies_Of_Document >1:

    if Document_number >=1:
        print('Here are your copies.')
    break


# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 

Light_for_stoplight= ( 'go_Light + slowdown_Light + stop_Light')
go_Light='30'
slowdown_Light='30'
stop_Light='30'
while Light_for_stoplight >= '90':

    if go_Light >='30':
        print('Change light 1.')
    
    if slowdown_Light>= '30':
        print('Change light 2.')


    if stop_Light >= '30':
        print('Change light 3')
    else:
        print('Go')
    break

# 4. Think of a scenario where you would use a while loop and the break keyword. 
# Then write down and describe it.  
# This does not need to be a code example.

# When you make a stop light program and you use after every 30 seconds with the go light, the slow 
# down light and stop light.


# 5. Think of a  scenario where you would use a while loop and a Create a while and the continue keyword.
# Then write down and describe it.  
# This does not need to be a code example.

#When a fan is turned on it goes on continuously without stopping till you turn it off.








# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change. 