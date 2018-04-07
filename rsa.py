import random

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def gcd(n, m):
    if n < m:
        tmp = n
        n=m
        m=tmp
    while m!=0:
        n, m = m, n%m
    return n

def extEuclid(e, phi):
    t1 = 0
    t2 = 1
    y1 = 1
    d = 0
    t_phi = phi

    while e > 0:
        tmp1 = t_phi/e
        tmp2 = t_phi - tmp1 * e
        t_phi = e
        e = tmp2

        x = t2- tmp1* t1
        y = d - tmp1 * y1

        t2 = t1
        t1 = x
        d = y1
        y1 = y

    if t_phi == 1:
        return d + phi

def generateKey(p, q):
    if not(is_prime(p)) or not(is_prime(q)):
        raise "p and q should be prime"

    n = p*q
    phi = (p-1)*(q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)

    while g!=1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = extEuclid(e, phi)

    return ((e, n) , (d, n))

def encrypt(key, m):
    e, n = key
    # for i in m:
    #     print ord(i)
    c = [(ord(i) ** e ) % n for i in m]
    return c

def decrypt(key, c):
    d, n = key
    # for i in c:
    #     print (i ** d ) %n
    m = [chr((i ** d) % n) for i in c]
    # print "here ", m
    return ''.join(m)

if __name__ == '__main__':
    p = int(raw_input("Enter the firstprime number: "))
    q = int(raw_input("Enter the second prime number:"))
    public, private = generateKey(p, q)
    print "Keys are: ", public, " " , private
    m = raw_input("Enter the message to encrypt: ")
    c = encrypt(public, m)
    print "Your encrypted message is: ", ''.join(map(lambda x: str(x), c))
    m = decrypt(private, c)
    print "Your decrypted message is: "
    print m
