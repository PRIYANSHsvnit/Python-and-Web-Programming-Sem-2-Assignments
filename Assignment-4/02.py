# Sherlock anbd Squares

def sherlockholmes(num1,num2):
    count = 0
    for i in range(num1,num2+1):
        if i in [j**2 for j in range(num2+1)]:
          count +=1

    return count

c = int(input("Enter Number of TC = \n"))

for i in range(c):
   a = int(input("Enter Starting Number = \n\n"))
   b = int(input("Enter Ending Number = \n"))

   print(f"\nNumber of Squares incl of A and B = {sherlockholmes(a,b)}")