# Implementing rfind

st = str(input("Input String = \n"))
s_1 = str(input("Enter the string to search in string S = \n"))

il = 0
jl = 0

for _ in st:
    il +=1

for _ in s_1:
    jl += 1

t = il - jl

while t>=0 :
    flag = True

    for i in range(jl):
        if st[t+i] != s_1[i]:
            flag = False
            break
        
    if flag:
        print(f"Found , Index = {t} \n")

    else:
        print("Not found \n")

    t =-1