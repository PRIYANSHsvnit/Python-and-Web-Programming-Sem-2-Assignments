# Inplementing rindex

st_1 = str(input("Enter String = \n"))

st_2 = str(input("Enter to search = \n"))

l = 0
m = 0

for _ in st_1:
    l +=1

for _ in st_2:
    m +=1

for i in range(l - m,-1,-1):
    if st_1[i:i+m] == st_2 :
        print(i,sep = '\t')