# Create Lists and solve following tasks

l_1 = []   # Creating an empty list

for i in range(50) :
    l_1.append(i)       # Taking input of numbers from range function with for loop

print(l_1)

print("\n")

l_2 = []  # Empty list

for i in range(1,51) :
    l_2.append(i**2)   # Taking input of numbers as their square respectively

print(l_2)

print("\n")

l_3 = []

# for i in range(1,27) :
#     string_1 = ''      # Creating an empty string
#     temp = i
#     while(i>0) :
#         string_1 += chr(temp+96)   # adding empty string with characters
#         i -=1
    
#     l_3.append(string_1)    # appending string into list created

# print(l_3)

for i in range(27):
    l_3.append(chr(i+97)*(i+1))

print(l_3)    