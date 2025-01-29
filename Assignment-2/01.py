# Word in word Capitalize

# a = str(input("Enter the word in which you want your word to be capatilize = \n"))

# b = str(input("Enter the word you want to capatilize in bigger word = \n"))

# c = list(b)
# d = list(a)

# for i,j in enumerate(d):
#     if j in c :
#        d[i] = j.upper()

# e = ''.join(d)

# print(e)

w = str(input("Eneter Word = \n"))

x = list(w)

for i in range(1,len(x),2):
    x[i] = x[i].upper()

y = ''.join(x)

print(y)