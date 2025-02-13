# OOPS

class Passwordmanager:
    def __init__(self,listx):
        self.passlist = listx

    def get_pass(self):
        return self.passlist[len(self.passlist)-1]
    
    def set_pass(self,newpass):
        if not newpass in self.passlist:
            (self.passlist).append(newpass)
            return "Password Changed Successfully\n"

        else:
            return 0
    
    def is_correct(self,passcheck):
        if passcheck == self.passlist[len(self.passlist)-1]:
            return True
        
        else:
            return False
        
a = []

b = int(input("Enter Number of Passwords consisting both New and Old ones , Enter Current Password in Last = \n"))

for i in range(b):
    l = input("Enter Password = \n")
    a.append(l)

person = Passwordmanager(a)

print(f"Current Password = {person.get_pass()}\n")

while(True):
    c = input("Enter Password you wanna change = \n")

    if person.set_pass(c):
        print(person.set_pass(c))
        break

    print("TRY AGAIN!\n")

d = input("Enter Password You Wanna check with Current One = \n")
print(f"The Password is {person.is_correct(d)}")