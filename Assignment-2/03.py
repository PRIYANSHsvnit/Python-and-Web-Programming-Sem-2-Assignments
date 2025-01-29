#Find Digits

t = int(input("Enter Number of test cases = \n"))

for k in range(t):
    a = (input("Enter Number N = \n"))
    b = int(a)

    u = [int(d) for d in a]

    for i,j in enumerate(u):
    
        if(b%j == 0):
         print(f"Index = {i}  have number = {j}")