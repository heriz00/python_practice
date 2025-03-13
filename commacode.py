def commaSep(newList):
    
    newString = ""
    
    for index, item in enumerate(newList):
        
        if len(newList) > 1 and len(newList) != 2:
            
            if index < len(newList) - 1:
                newString = newString + str(item) + ", " 

            else:
                newString = newString + "& " + str(item)
         
        elif len(newList) == 2:
            
            if index < len(newList) - 1:
                newString =  newString + str(item) + " & " 

            else:
                newString = newString + str(item)
            
           
        else: 
            newString = str(item)
            
    return newString
    
spam = input("Give me any list: ")

if "," not in spam:
    newList = spam.split(" ")

else:
    newList = spam.split(", ")

result = commaSep(newList)

print(result)



