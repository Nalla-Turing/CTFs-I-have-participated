from BitVector import *
from Reverse import *
from AESencyptfunc import *

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


def func2():


#code is okay till here for func1
    plaintextseg = "mynameismrinaldhmynameismrinaldhmynameismrinaldh"
    PassPhrase = "EncryptedLessons"
    PassPhrase=BitVector(textstring=PassPhrase)
    bv1 = BitVector(textstring=plaintextseg)
    bv2 = PassPhrase
    resultbv=bv1^bv2
    myhexresult = resultbv.get_bitvector_in_hex()

    print(myhexresult)

    for x in range(1, 5):
        temp1=subbyte(myhexresult)
        temp2=shiftrow(temp1)
        bv3 = BitVector(hexstring=temp2)
        newbvashex=mixcolumn(bv3)
        newbv=BitVector(hexstring=newbvashex)
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkeys[x-1])
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()

    temp1=subbyte(myhexresult)
    temp2=temp1
    bv3 = BitVector(hexstring=temp2)
    newbvashex=mixcolumn(bv3)
    newbv=BitVector(hexstring=newbvashex)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkeys[4])
    resultbv = bv1 ^ bv2
    myhexresult = resultbv.get_bitvector_in_hex()

    for x in range(6, 9):
        temp1=subbyte(myhexresult)
        temp2=shiftrow(temp1)
        bv3 = BitVector(hexstring=temp2)
        newbvashex=mixcolumn(bv3)
        newbv=BitVector(hexstring=newbvashex)
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkeys[x-1])
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()

    myhexstring = resultbv.get_bitvector_in_hex()
    temp1=subbyte(myhexstring)
    temp2=shiftrow(temp1)
    newbv = BitVector(hexstring=temp2)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkeys[8])
    resultbv = bv1 ^ bv2
    myhexresult = resultbv.get_bitvector_in_hex()

    myhexstring = resultbv.get_bitvector_in_hex()
    temp1=subbyte(myhexstring)
    temp2=shiftrow(temp1)
    bv3 = BitVector(hexstring=temp2)
    newbvashex=mixcolumn(bv3)
    newbv=BitVector(hexstring=newbvashex)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkeys[9])
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()

    return myhexstring

def func1(resultbv):
    outputtext = ""
    ciphertext = "aa72fdd42a0befa9a7b4efcf62daccb3ae75f6db23a609b50c5b5c3166603ca95ec10a619ff8f4a55103ad93df30745d1d95fbd9db0c58e30e5d503f9b6b82e8ee3b0975cfb10f1552040a63846481f24f665385c30755f0bcbbf6c572698d52"
    start = 0
    end = 0
    length = len(ciphertext)
    loopmsg = math.ceil(length / 32) + 1

    for x in range(1,loopmsg):
        if(end+32<=length):
            text = ciphertext[start:end+32]
        resultbv = BitVector(hexstring = text)
        resultbv = BitVector(bitlist = resultbv)
        bv2 = BitVector(hexstring=roundkeys[9]) 
        bv1 = bv2 ^ resultbv
        newbvashex=inverse_mixcolumn(bv1)
        print(newbvashex)
        temp2=reverse_shiftrow(newbvashex)
        print("temp2     ",temp2)
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

        resultbv = result1
        PassPhrase = "EncryptedLessons"
        PassPhrase=BitVector(textstring=PassPhrase)
        bv2 = PassPhrase
        text=resultbv^bv2
        text = text.get_bitvector_in_ascii()
        start = start + 32 
        end = end + 32
        outputtext += text
    print(outputtext)
#Code is okay till here for func2

def func3():
    outputtext = ""
    ciphertext = "cb98a887543c90ddb81d288f7e31ebdb850c961462a27f0f307c765f34da9fb6e2b55355f95d76376f1c82f4161308b7ee3b0975cfb10f1552040a63846481f24f665385c30755f0bcbbf6c572698d52"
    start = 0
    end = 0
    length = len(ciphertext)
    loopmsg = math.ceil(length / 32) + 1

    for x in range(1,loopmsg):
        if(end+32<=length):
            text = ciphertext[start:end+32]
        resultbv = BitVector(hexstring = text)
        resultbv = BitVector(bitlist = resultbv)
        bv2 = BitVector(hexstring=roundkeys[9]) 
        bv1 = bv2 ^ resultbv
        bv1= bv1.get_bitvector_in_hex()
        temp2=reverse_shiftrow(bv1)
        print("new temp2      ",temp2)
        temp1=reverse_subbyte(temp2)
        result1 = BitVector(hexstring = temp1)

        bv2 = BitVector(hexstring=roundkeys[8])
        resultbv =BitVector(bitlist = result1)
        bv1 = bv2 ^ resultbv
        bv1 = inverse_mixcolumn(bv1)
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
        temp2 = reverse_shiftrow(newbvashex)
        temp1 = reverse_subbyte(temp2)
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
        print("temp1    ",temp1)

        resultbv = result1
        PassPhrase = "EncryptedLessons"
        PassPhrase=BitVector(textstring=PassPhrase)
        bv2 = PassPhrase
        text=resultbv^bv2
        text = text.get_bitvector_in_ascii()

        print(text)
        start = start + 32 
        end = end + 32
        outputtext += text
    print(outputtext)

a = func2()
func1(a)
func3()