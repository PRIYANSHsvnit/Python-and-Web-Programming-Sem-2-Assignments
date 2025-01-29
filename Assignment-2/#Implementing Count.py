#Implementing Count

s_1 = str(input("Input a String = \n"))

count = 0
i=0

# try :
#     while True:
#         x = s_1[i]
#         i +=1
#         count +=1

# except IndexError:
#     pass

for _ in s_1:
    count +=1

print(f"Number of Characters in Given String = {count}")