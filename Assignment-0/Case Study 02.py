# Codedocs Admin Kidnap

T = int(input("Enter total number of Test cases = "))  # Enter Number of Test cases

N = int(input("Enter number of Boxes = "))             # Enter number of boxes

X = int(input("Enter the Xth box Number = "))          # Enter the numnber of bax in which gold coin is initially present

S = int(input("Enter number of Swaps = "))             # Number of swaps to play game

i = 0

while i < T:
    for i in range(S):

        A=int(input("Enter A = "))                     # Enter the index of boxes to play game with
        B=int(input("Enter B = "))                     

        if (B == X) :
            temp=A
            A=X
            X=temp
                                                       # Swap from A to B or vice versa
        elif (A==X) :
            temp=B
            B=X
            X=temp

i+=1

print(X)                                               # Number of swaps till end of game