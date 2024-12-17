from AESencyptfunc import *  # Ensure the decryption functions are imported
from Reverse import *
from BitVector import *
from Reverse import *
from BitVector import *
import math
import sys

'''if len(sys.argv) != 3:
    sys.exit("Error, script needs two command-line arguments. (cipherhex.txt File and output Plaintext.txt File)")

PassPhrase = "EncryptedLessons"

# Read the ciphertext
file = open(sys.argv[1], "r")
ciphertext = file.read()
print("The ciphertext is:\n%s\n" % ciphertext)
file.close()

start = 0
end = 0
length = len(ciphertext)
loopmsg = math.ceil(length / 32) + 1 # Each 16-character plaintext block becomes 32 hex chars in ciphertext
outputtext = ""

roundkeys = [
    '81aabaabf8dacece9c96abbdeff9c5ce',
    'd0c5deee281f1020b489bb9d5b707e53',
    '0e11271f260e373f92878ca2c9f7f2f1',
    '5b497c7c7d474b43efc0c7e126373510',
    'd6d6c6f0ab918db344514a5262667f42',
    '3a032e389192a38bd5c3e9d9b7a5969b',
    '753f1f25e4adbcae316e557786cbc3ec',
    '9456590970fbe5a74195b0d0c75e733c',
    '7b8fcf640b742ac34ae19a138dbfe92f',
    '58cc4a4353b860801959fa9394e613bc'
]

for x in range(1,loopmsg):
    if(end+32<=length):
        text = ciphertext[start:end+32]
    resultbv = BitVector(hexstring = text)
    resultbv = BitVector(bitlist = resultbv)
    bv2 = BitVector(hexstring=roundkeys[9]) 
    bv1 = bv2 ^ resultbv
    newbvashex=inverse_mixcolumn(bv1)
    temp2=reverse_shiftrow(newbvashex)
    temp1=reverse_subbyte(temp2)
    result1 = BitVector(hexstring = temp1)

    bv2 = BitVector(hexstring=roundkeys[8])
    resultbv =BitVector(bitlist = result1)
    bv1 = bv2 ^ resultbv
    bv1 = bv1.get_bitvector_in_hex()
    temp2 = reverse_shiftrow(bv1)
    temp1 = reverse_subbyte(temp2)
    result1 = BitVector(hexstring = temp1)

    for x in range(8,5,-1):
        bv2 = BitVector(hexstring=roundkeys[x-1])
        resultbv =BitVector(bitlist = result1)
        bv1 = bv2 ^ resultbv
        newbvashex=inverse_mixcolumn(bv1)
        temp2 = reverse_shiftrow(newbvashex)
        temp1 = reverse_subbyte(temp2)
        result1 = BitVector(hexstring = temp1)
    
    bv2 = BitVector(hexstring=roundkeys[4])
    resultbv =BitVector(bitlist = result1)
    bv1 = bv2 ^ resultbv
    newbvashex=inverse_mixcolumn(bv1)
    temp1 = reverse_subbyte(newbvashex)
    result1 = BitVector(hexstring = temp1)

    for x in range(4,0,-1):
        bv2 = BitVector(hexstring=roundkeys[x-1])
        resultbv =BitVector(bitlist = result1)
        bv1 = bv2 ^ resultbv
        newbvashex=inverse_mixcolumn(bv1)
        temp2 = reverse_shiftrow(newbvashex)
        temp1 = reverse_subbyte(temp2)
        result1 = BitVector(hexstring = temp1)

    resultbv = result1.get_bitvector_in_hex()
    print(temp1)

    resultbv = result1
    PassPhrase = "EncryptedLessons"
    PassPhrase=BitVector(textstring=PassPhrase)
    bv2 = PassPhrase
    text=resultbv^bv2
    text = text.get_bitvector_in_ascii()

    print(text)
    start = start + 32 
    end = end + 32
    FILEOUT.write(text)

# Write the decrypted text to the output file
fileout = open(sys.argv[2], "w")
fileout.write(outputtext)
fileout.close()

print("Decryption complete. The plaintext message is saved in: %s" % sys.argv[2])'''

a = "cb98a887543c90ddb81d288f7e31ebdb"
a = BitVector(hexstring = a)
resultbv = BitVector(bitlist = a)
print(resultbv)
c = BitVector(hexstring = '58cc4a4353b860801959fa9394e613bc')
print(c)
print(resultbv^c)
d=(resultbv^c).get_bitvector_in_hex()
print(d)
e = reverse_shiftrow(d)
print(BitVector(textstring = e))
