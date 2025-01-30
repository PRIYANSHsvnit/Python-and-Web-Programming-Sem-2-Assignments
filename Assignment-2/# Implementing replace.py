# Implementing replace

s = str(input("enter string = \n"))
s1 = str(input("To replace = \n"))
s2 = str(input("To replace with = \n"))
result =""

a=0
b=0
c=0
i=0

for _ in s:
    a +=1

for _ in s1:
    b +=1

for _ in s2:
    c +=1

while i<a :

    flag = True

    for j in range(b):
        if (i+j)>=a or s[i+j] != s1[j]:
            flag = False
            break

    if flag:
        
        for z in range(c):
            result += s2[z]
        i+=b

    else:
        result += s[i]
        i+=1


print(result)