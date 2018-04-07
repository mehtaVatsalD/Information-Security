
def findPrimitiveRoot(p):
    for r in range(1, p):
        l = [0] * p
        flag = 0
        for x in range(0, p-1):
            temp = ( r ** x ) % p
            if temp in l:
                flag = 1
                break
            else:
                l[temp] = temp
        if flag == 0:
            return r

def dh(a, b, e, p):
    alice = (e ** a) % p
    bob = (e ** b) % p
    k1 = (bob ** a) % p
    k2 = (alice ** b) % p
    if k1 == k2:
        return k1

if __name__ == '__main__':
    p = int(raw_input("Enter a prime Number: "))
    e = findPrimitiveRoot(p)
    print "Public Keys are: ", p ," ", e;
    a = int(raw_input("Enter Alice's Private Number: "))
    b = int(raw_input("Enter Bob's Private Number: "))
    key = dh(a, b, e, p)
    print "Exchanged key is: ", key
