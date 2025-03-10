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

message = '''Dear Heriz of 2026,
I hope you're doing well. I hope I made you proud. I hope when you look back, you are satisfied. 
I hope you made it. 
I hope you are happy.
I hope you still work hard. 
I hope everything worked out. 
Yours, 
Heriz of 2025'''

print(message)
new_message = message.split("\n")
print (new_message)
new_new_message = ''.join(message)
print(new_new_message)

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

name = "   Heriz Bista    "
print(name.strip())
print(name.lstrip())
print(name.rstrip())