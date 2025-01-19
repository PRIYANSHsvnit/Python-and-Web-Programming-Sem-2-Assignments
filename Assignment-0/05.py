# Let say a number A to find its Table till what we want

a = int(input("Enter Number A = "))  # Input of numnber A

b = int(input("Table Till = ")) # Table till That Number

for i in range(1,b+1) :
    print(a,"x",i," = ",a*i)  # printing table of A