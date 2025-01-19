# Let Number A , to find it's Factorial

a=int(input("Enter Number A = ")) # Input of Number A

fact = 1

while(a>0) :
    fact = fact * a     # Loop To calculate of factorial of An Number
    a -= 1

print("Factorial Of Given Number of A = ",fact)