while True:
    print("Give me your age: ")
    age = input()
    print("Give me your password:")
    password = input()
    
    if age.isdecimal() and password.isalnum():
        
        if password.startswith("Heriz") or password.endswith("Bista"):
            print("\nYou cannot add name to your password.\n")
            continue
        
        else:
            print(f'''You've given correct information.
Your given age is {age} and your password is {password}''')
            break
    else:
        print("Wrong information. Do it again")
        continue
    