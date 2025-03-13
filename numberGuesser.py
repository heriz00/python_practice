
def start():
    print ("\n I am thinking of one number between 1 to 40. Can you guess the number in three tries? \n") 

def specialExit(user_input):
    if user_input == 0:
        print("\nThe game has been aborted. Thank you.\n")
        return True
    
    elif user_input == 69:
        print("\nThe game has been restarted. Play again!\n")
        return True
        
number = 33        
start()
for i in range(1,4):
    user_input = int (input ("Your " + str(i) +  " try: " ))
    if user_input == number and i == 1:
        print ("\nVoila! You got it right in one shot. Bravo.")
        break
    elif user_input == number and i >= 2:
        print ("\nVoila! You got it right.")
        break
    elif user_input != number:
        counter = 0
        while counter <= 3: 
            if 30 < user_input < 35 and user_input != number:
                print ("\nYou are very close. Try Again. \n")
                counter += 1
                break            
            elif user_input > 100:
                print ("\nYo! Chill out. Way too far. Try Again. \n")
                counter += 1
                break
            elif user_input != 0 and user_input != 69:
                print (" \nSorry mate! Try Again. \n")
                counter += 1
                break
            elif user_input == 0 or user_input == 69:
                specialExit()
                break
        if user_input == 0:
            break
        elif user_input == 69:
            start()
        else: print ("\nYou have " + str(3-i) + " try left.\n")
        if i > 3:
            print ("\nSorry! Game Over. Better Luck Next Time.")
            
if user_input == number and i != 1:
    print ("\nYou got it right in " + str(i) + " try/tries")

exit_input = str(input ("\nDo you want to play again (Y/N)?: "))

while True:
    if exit_input != "Y" and exit_input != "N":
        exit_input = str(input ("\nInvalid Input! Please enter again: "))
        
    elif exit_input == "Y" or exit_input == "N":
        if exit_input == "Y":
            start()
            
        elif exit_input == "N":
            print ("Hope you will be back soon. Ciao!")
            break
