# Implementing rsplit

st = str(input("Input String = \n"))
dem = str(input("Input patrameter = \n"))
n = int(input("Enter the times of splitting = \n"))

st1 = []
a=0

for _ in st:
    a +=1
prev = a
j = prev

count = 0
for i in range(prev - 1,0,-1):
    if st[i] == dem:
        st1.append(st[i+1:j])
        j = i
        count +=1

        if count == n:
            break

st1.append(st[0])

st2 = st1[::-1]

print(st2)