import random

coin = []

i = 1
counter = 0
h_streak = 0
t_streak = 0

while i <= 100000:
    flip = random.choice(["H","T"])
    coin.append(flip)
    i += 1

for index,item in enumerate(coin):
    
    last_item = []
    
    if item == 'H':
        last_item.append('H')
        
        if 'T' not in last_item and counter == 6:
            h_streak = h_streak + 1
            counter = 0
                
    else:
        last_item.append("T")
    
        if 'H' not in last_item and len(last_item) == counter:
            t_streak = t_streak + 1
            counter = 0
            
    counter += 1
    
print(f"The streak of head is {h_streak}")
print(f"The streak of tail is {t_streak}")
    