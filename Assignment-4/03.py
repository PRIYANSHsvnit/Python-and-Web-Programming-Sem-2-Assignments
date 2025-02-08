import string

st = input("Enter string = \n\n")

st = st.lower()

flag = True

for i in string.ascii_lowercase:
    if i in st:
        flag = True

    else:
        print("\nNot A Pangram \n\n")
        flag = False
        break

if flag:
    print("\nIs Pangram \n\n")