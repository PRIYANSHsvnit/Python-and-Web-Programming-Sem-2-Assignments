def magicsquare(n):

    ms = [[0 for i in range(n)] for i in range(n)]

    a,b = n//2, n-1

    for num in range(1,n**2+1):

        if ms[a][b] != 0:
            a += 1
            b -= 2
            continue
        
        ms[a][b] = num

        x,y = (a-1)%n,(b+1)%n

        if ms[x][y] != 0:
            a = (a+1)%n

        else:
            a,b = x,y

    return ms

n = int(input("Enter odd number = "))

if n % 2 == 0:
    print("Only for Odd Numbers \n")

else:
    result = magicsquare(n)

    for row in result:
        print(row)