# Scale conversions

a = int(input("Eneter Length in Feets = "))

print(''' 
      Enter 1 to convert in inches 
      Enter 2 to convert in yards 
      Enter 3 to convert in miles
      Enter 4 to convert in MM
      Enter 5 to convert in CM
      Enter 6 to convert in M
      Enter 7 to convert in yards KM ''')

# print()

# b = int(input("Enter option = "))

# match(b) :
#     case 1 :
#         print(12*a)

#     case 2 :
#         print(a/3)

#     case 3 :
#         print(a/5280)

#     case 4 :
#         print(304.8*a)

#     case 5 :
#         print(30.48*a)

#     case 6 :
#         print(0.3048*a)

#     case 7 :
#         print(a/3281)

#     case _ :
#         print("Invalid Case")

l = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]

b = int(input("\nEnter option = "))

print("\nOperation Result = ",l[b-1]*a)