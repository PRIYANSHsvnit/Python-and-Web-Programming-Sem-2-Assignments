# MAX XoR

'''def maxxor(l,r):
    maxx = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            maxx = max(maxx,i^j)

    return maxx'''

def maxxor(l,r):
    maxx = 1
    xor = l^r
    
    while(xor>0):
        maxx = maxx*2
        xor = xor//2

    return maxx-1

l = int(input("Enter L = \n"))
r = int(input("Enter R = \n"))

print(f"MAX XOR between L and R = {maxxor(l,r)}\n")