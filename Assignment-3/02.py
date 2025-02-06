def isfibo(num):
    
    x = 0
    y = 1
    
   
    while x < num:
        x, y = y, x + y

    if x == num:
        return "\nIs Fibo"
    else:
        return "\nNot Fibo"

t = int(input("Enter Number of test cases = \n"))

for j in range(t):
    a = int(input("Enter the number to check = \n"))
    result = isfibo(a)
    print(result)