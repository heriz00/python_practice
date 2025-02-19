def collatz(number):
    value1 = number // 2
    value2 = 3*number+1
    try:
        if (number % 2 == 0):
            print ("The value for even is: " + str(value1))
            return value1
        else:
            print ("The value for odd is: " + str(value2))
            return value2 
        
    except ValueError:
        print("Invalid Response.")
        
def user_input():
    while True:
        try:
            number = int(input("Give me your input for The Collatz Sequence Problem: "))
            return number

        except ValueError:
            print ("You have entered incorrect value. Please try again!")

    
correct_number = user_input()

while correct_number != 1:
        if correct_number % 2 == 0:
            correct_number = collatz(correct_number)
        else:
            correct_number = collatz(correct_number)
            
print("The number is: " + str(correct_number))

