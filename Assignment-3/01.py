# Implementing Digital Root

# def digiroot(num):
#     digi = num
#     digi1 = -1
#     digi2 = 0
    
#     while(digi1 not in range(10)):
#         for i in range(len(digi)):
#            int(digi2)
#            digi2 += int(digi[i])

#         digi1 = digi2

#         str(digi2)
#         digi = digi2


#     return int(digi)

def digiroot(num):
    while(num not in range(10)):
        num = sum(int(i) for i in str(num))

    return (num)

a = int(input("enter the number of which you want digital root = \n"))

print(f"Digi root = {digiroot(a)}")