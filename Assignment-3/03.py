# Utopian tree

def tree(a,b):
    
    for i in range(1,b+1):
     if i%2 != 0 :
        a = a*2

     else:
        a +=1

    return a

c = int(input("enter number of TC = \n"))

for i in range(c):
   b = int(input("Number of cycles = \n"))
   x = tree(1,b)
   print(f"Final height of tree = {x}\n")