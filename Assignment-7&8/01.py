# Linked LIst

class node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new = node(data)
        new.next = self.head
        self.head = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def delete(self, num):
        current = self.head

        if current and current.data == num:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != num:
            prev = current
            current = current.next

        if current is None:
            print("Key not found in the list.")
            return

        prev.next = current.next
        current = None

a = int(input("Enter How Many LL You want = \n"))
o = LL()

for i in range(a):
    c = int(input("Enter Data = \n"))
    o.insert(c)

print("\nDisplay...\n\n")
o.display()

d = int(input("\n\nEnter the node you wanna delete = \n"))
o.delete(d)

print("\nDisplay...\n\n")
o.display()