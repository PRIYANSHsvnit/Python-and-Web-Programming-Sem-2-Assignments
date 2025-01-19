# Let say two numbers A and B to swap them

a = int(input("Enter A = "))
b = int(input("Enter B = ")) # Input of Numbers

print("Number A = ",a, ", Number B = ",b) # Printing them before Swapping

a = a+b
b = a-b    # Swapping
a = a-b

print("Number A after swapping = ",a,"\nNumber B after swapping = ",b)  