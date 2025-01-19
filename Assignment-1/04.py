# Equivalence class

from collections import defaultdict   # Module imported

def equiclass(num_1,num_2) :
    return (num_1)%(num_2)       # Function

l = []

u = []   # Empty list

for i in range(1,1001) :    # Numbers in list
    l.append(i)

dict_1 = defaultdict(list)   # Empty dictionary

x = int(input("Enter Number to divide from from = "))       # Divisor

for num in l :
    key = equiclass(num,x)     # Remainder
    dict_1[key].append(num)    # Number

for key,lis in dict_1.items() :
    print(f"For Remainder {key} , the list is {lis} \n")

    u = list(set(u).union(set(lis)))      # Union of all rquivalence classes

print(u"\n")

if(u == l) :

    print("Validity successful")