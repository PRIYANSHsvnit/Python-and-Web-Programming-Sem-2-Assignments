# min distance between two points in 3-D

from collections import defaultdict  # Module

import math  # Module

def dis(y,z) :
    return math.sqrt((y[0]-z[0])**2 + (y[1]-z[1])**2 + (y[2]-z[2])**2)  # Function for distance

dict = defaultdict(list)
dict_1 = defaultdict(list)     # Empty Dictionaries

n = int(input("Enter Number of Points = "))  # Number of points

for i in range(n) :
    l = []

    for j in range(3) :
        l.append(int(input(f"Enter Element {j+1} for point {i+1} = ")))    # Input of 3 numbers for a point

    dict[i] = l

for m in range(n-1) :
    l_1 = []
    for o in range(n) :
       if(o == m) :
        continue
       
       else : l_1.append(((dis(dict.get(m),dict.get(o))),o))     # Distance of one from others
      
    l_1.sort()  # Sorting in ascending order to get minimum distance to find nearest point
    
    md,t = l_1[0]  # nearest point index given to t

    dict_1[m]={
       "point" : dict.get(m),
       "Nearest Point" : dict.get(t),          # Giving input to these terms as point , its nearest point and distance
       "Distance" : md,
    }

for i,j in dict_1.items() :
    print(i,j)
    print("\n")