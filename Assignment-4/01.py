#Love Letter se Chedkaad

def palindrome(c):
    a = list(c)

    n = len(c)
    m = n-1

    i = (n//2)-1
    l = 0
    o = 0

    count = 0

    while(i>=0):
        if n%2 == 0:
            if a[i] == a[m-i]:
                i -= 1

            else:
                l = min(ord(a[i]),ord(a[m-i]))
                o = max(ord(a[i]),ord(a[m-i]))
                count += o-l
                i -=1

        else:
            if a[i] == a[m-i]:
                i -= 1

            else:
                l = min(ord(a[i]),ord(a[m-i]))
                o = max(ord(a[i]),ord(a[m-i]))
                count += o-l
                i -=1

    return count

k = int(input("Enter Number of Test Cases = \n"))

for i in range(k):
    c = input("Enter String = \n")

    print(f"\nNumber of Operations = {palindrome(c)} \n")