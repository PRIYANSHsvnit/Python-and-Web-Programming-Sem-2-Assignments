# Let say number A to find it's Reverse

a = int(input("Enter number A = "))

s = 0

while(a>0) :
    q = a%10
    s = s*10 + q
    a = a//10

print("Reverse of Given Number A = ",s)