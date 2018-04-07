IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

KP56 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

KP48 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

EB = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

SB = [

[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],

[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]


SP = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] #1 2 9 16 bits only 1 shift rest keys 2 shifts

def bval(val, size):
    b_val = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:] #[2:] is used to remove 0b prefix attached to return of bin() func
    if len(b_val) > size:
        print "Binary value greater than bits"
    while len(b_val) < size:
        b_val = "0" + b_val #padding prev bits to not change the actual value
    return b_val

def nsplit(l, n):
    return [l[k:k+n] for k in range(0, len(l), n)]

def s_to_b(text):
    res = list()
    for char in text:
        b_val = bval(char, 8)
        res.extend([int(x) for x in list(b_val)]) #appends the individual elements in the list. if .append is used then the whole list gets added as an element
    return res

def b_to_s(bits):
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(bits,8)]])
    return res#can do the same in extended for loop too

ENCRYPT = 1
DECRYPT = 0

class des():
    def __init__(self): #as a constructor. creates self having properties that is passed to each method as a first arg.
        self.keyword = None
        self.text = None
        self.keys = list()

    def permute(self, block, table): #can be used for expansion too due to mapping shown in table
        return [block[x-1] for x in table]# here as per the table, mapping is done. hence block values gets restricted as size of table

    def xor(self, t1, t2):
        return [x^y for x,y in zip(t1,t2)] # zip take corresponding values from both the params; 1 to 1 maping

    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    def addP(self):
        print "entered"
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len) #public key padding technique

    def remP(self, res):
        pad_len = ord(res[-1])
        return res[:-pad_len]

    def makeKeys(self):
        self.keys = []
        key = s_to_b(self.keyword)
        key = self.permute(key, KP56)
        l, r = nsplit(key, 28)
        for i in range(16):
            l, r = self.shift(l, r, SHIFT[i])
            tmp = l + r #Merge them
            self.keys.append(self.permute(tmp, KP48))

    def sbox(self, d_e):
        subblocks = nsplit(d_e, 6)#Split bit array into sublist of 6 bits
        result = list()
        for i in range(len(subblocks)): #For all the sublists
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)#Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
            val = SB[i][row][column] #Take the value in the SBOX appropriated for the round (i)

            bin = bval(val, 4)#Convert the value to binary
            result += [int(x) for x in bin]#And append it to the resulting list
        # print result
        return result

    def process(self, key, text, type=ENCRYPT, padding=False):

        if len(key) < 8:
            print "key should be of 8 bytes"
        elif len(key) > 8:
            key = key[:8]

        self.keyword = key
        self.text = text

        if padding and type==ENCRYPT:
            self.addP()
        elif len(self.text) %8 != 0:
            print "data must be of size multiple of 8"

        # print self.text
        #key handling process
        self.makeKeys()
        text_b = nsplit(self.text, 8)
        result = list()
        # print self.keys[15]
        for b in text_b:
            b = s_to_b(b)
            b = self.permute(b, IP) #initial permutation
            l,r  = nsplit(b, 32)
            # print l
            temp = None
            for i in range(16):
                r_k = self.permute(r, EB) #right to apply funtion to it
                if type==ENCRYPT:
                    temp = self.xor(r_k, self.keys[i])
                else:
                    temp = self.xor(r_k, self.keys[15-i])

                temp = self.sbox(temp)
                temp = self.permute(temp, SP)
                temp = self.xor(l, temp)
                l = r
                r = temp
            result += self.permute(r+l, FP)
        final = b_to_s(result)

        print final
        if padding and type==DECRYPT:
            return self.remP(final)
        else:
            return final

    def enc(self, key, text, padding=False):
        return self.process(key, text, ENCRYPT, padding)

    def dec(self, key, text, padding=False):
        return self.process(key, text, DECRYPT, padding)

if __name__ == '__main__':
    key = "abcdefgh"
    text =  "Hello wo"
    d = des()
    res1 = d.enc(key, text, False)
    res2 = d.dec(key, res1, False)
    print "Encrypted text %r" % res1
    print "Decrypted text " + res2
