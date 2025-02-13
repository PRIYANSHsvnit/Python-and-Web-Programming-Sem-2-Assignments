#Cut and Pieces

def choco(num):
    if(not num%2):
       x = num//2
       return (x)**2
    
    else:
        x = num//2
        return (x)*(x + 1)
    
b = int(input("Enter Number of TC = \n"))

for i in range(b):
    a = int(input("Enter Number of Cuts = \n"))
    print(f"MAX Number of pieces of chocolate = {choco(a)}")