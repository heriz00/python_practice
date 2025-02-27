#coinflipstreakcodelearning

import random

coin = []

i = 1
h_flip = 0
t_flip = 0
h_streak = 0
t_streak = 0

while i <= 10000:
    flip = random.choice(["H","T"])
    coin.append(flip)
    i += 1


for flip in coin:
    
    if flip == 'H':
        h_flip += 1
        t_flip = 0
        
        if h_flip == 6:
            h_streak += 1
            h_flip = 0
                
    else:
        t_flip +=1
        h_flip = 0
        
        if t_flip ==6:
            t_streak += 1
            t_flip = 0
               
print(f"The streak of head is {h_streak}")
print(f"The streak of tail is {t_streak}")
    