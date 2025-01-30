#Implementing Count

s_1 = str(input("Input a String = \n"))
sub = str(input("Enter what to search = \n"))

count = 0
i=0

a = len(s_1)
b = len(sub)

for i in range(a-b+1):
    if s_1[i:i + b] == sub:
        count+=1

print(f"Number of Characters in Given String = {count}")