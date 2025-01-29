# Product name and their prices

dict_1 = {}     # Creating a empty dictionary

a = int(input("Enter The number of Products = \n"))

for i in range(a) :
    b = str(input(f"Enter Name of Product {i+1} = "))
    c = float(input(f"Enter Price for Product {i+1} = \n"))

    dict_1[b] = c

count = 0

d = str(input("Enter Product Name whose price you want to know = \n"))

# for i,j in dict_1.items() :
#     if(dict_1[d] == i):
#         print(f"{d} Have Price = {dict_1[d]} \n")
#         break
#     else :
#         count +=1

# if(count == len(dict_1)):
#     print("Product is not present in Dictionary \n")

if d in dict_1:
    print(f"{d} has a price of = {dict_1[d]}")
else:
    print("Product is not present in Dictionary \n")