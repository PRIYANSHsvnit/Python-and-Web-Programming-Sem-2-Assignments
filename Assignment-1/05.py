# Names of student

l = [] # Empty list

i =0

n = int(input("Enter number of students = "))  # Number of students

while(i<n) :
    string_1 = input(f"ENTER Name of Student {i+1} = ")  # String created to store names
    if(len(string_1)>15) :
    
        i-=1                    # Condition
        continue
    

    else :
    
         l.append(string_1)       # Name appended to list
    
    i+=1
    
for i in range(n) :
    print(l[i][::-1])    # Reverse print of names