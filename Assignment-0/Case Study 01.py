# Codedocs Admin Psycho

a = int(input("Enter Length of List = ")) # Enter Lenghth of list
l = [] # Empty list

for i in range(a):
    b = input(f"Enter Height of Person {i+1} = ")   # taking Input of List
    l.append(b)

el = [None]*(a)   # Creating Another Empty list 

i = 0

swap = 0

while(l != [])  :
    

    if(len(l) == 1) :
        el[i] = l[0]            # For odd length lists 
        del l[0]

    else :
        el[i] = min(l)
        el[a-1-i] = max(l)
                                       # For even length lists
        del l[l.index(min(l))]
        del l[l.index(max(l))]

    i += 1    
    swap += 1 

print(el)
print("Number Of Swap = ",swap)