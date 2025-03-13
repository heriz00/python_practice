def collatz(number):
    # For even numbers, return number // 2; for odd numbers, return 3 * number + 1
    return number // 2 if number % 2 == 0 else 3 * number + 1
        
def user_input():
    while True:
        try:
            number = int(input("Give me your input for The Collatz Sequence Problem: "))
            return number

        except ValueError:
            print ("You have entered incorrect value. Please try again!")

    
correct_number = user_input()

while correct_number != 1:
    correct_number = collatz(correct_number)
    print(f"The value is {correct_number}")
            
print(f"The final number is {correct_number}. Hence, the program stopped.")

