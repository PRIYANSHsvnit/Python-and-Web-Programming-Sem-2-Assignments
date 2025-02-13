#BiggerIsGreater

def lux(arr):
    arrl = list(arr)
    l = len(arr)
    
    i = l-2

    while(arrl[i]>=arrl[i+1] and i>=0):
        i -=1

    if i == -1:
        return "Already Sorted"
    
    j = l-1

    while(arrl[j]<=arrl[i]):
        j -=1

    arrl[i],arrl[j] = arrl[j],arrl[i]

    return "".join(arrl)

n = int(input("Enter Number of TC = \n"))

for i in range(n):
    a = input("\nEnter String = \n")
    b = lux(a)

    print("\nLEXO = \n")
    print(str(b))