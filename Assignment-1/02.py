# RAndom 0 and 1

import random   # Random module

l = [] # Empty list

for i in range(100) :
    l.append(random.randint(0,1))  # Appending random number between 0 and 1 in list created 

print(l)

mr = 0  # Max reading
cr = 0  # Current reading

for i in range(100) :
    if(l[i] == 1) :
        cr = 0
        continue

    else :
        cr +=1
        mr = max(mr,cr)

print("\n")
print(mr)    # Number of max zeroes together