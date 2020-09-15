'''
Created on 11. 4. 2019

@author: Kiara
'''
import sys
from ast import literal_eval

#prvocislo, pouziva se k modulu
Fp = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

# y^2 = x^3 + ax + b
a = -0x3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b

# (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 
#  0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
Px = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Py = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5

'''
Modular multiplicative inverse
Vypocita inverzni prvek k danemu cislu. Funguje jenom kdyz Fp je prvocislo  coz je
taky znamo jako modiv
'''
def mInverse(number):
    return pow(number, Fp-2, Fp)

'''
Secteni tech samych bodu, 2p, P+P
'''
def pDoubling():
    s1 = (3 * Px * Px) + a
    s2 = s1 * mInverse(2 * Py)
    s = s2 % Fp
    
    Rx = ((s * s) - (2 * Px)) % Fp
    
    Ry = (s * (Px - Rx) - Py) % Fp
    
    return (Rx, Ry)

'''
Secteni dvou rozdilnych bodu. vysledek predchazejici iterace se secte se zkladnim bodem
R + P, kde R je 2P.....XP
R je ve formatu Tuple
'''
def pAdding(R):
    s1 = R[1] - Py
    s2 = s1 * mInverse(R[0] - Px)
    s = s2 % Fp

    #R next x
    RNX = ((s * s) - Px - R[0]) % Fp
    
    RNY = (s * (Px - RNX) - Py) % Fp

    return (RNX, RNY)


'''
Nalezne private key k zadanemu public key Q
Q = k * P
hledame to k
'''    
def findPrivate(Q):
    if (Q[0] == Px and Q[1] == Py): #Public key je stejny jako zakldani bod, Q = 1*P
        return 1
    
    R = pDoubling() # 2P = P + P
    
    if (Q[0] == R[0] and Q[1] == R[1]):
        return 2
    
    #3P, 4P......... XP
    #TODO otestuj jak rychle to zvladne
    end = 200
    i = 3
    while i < end:
        R = pAdding(R) 
        
        if (Q[0] == R[0] and Q[1] == R[1]):
            return i  
        
        if (i + 1 == end): #prodlouzeni prohledavani, TODO popremyslej jestli to nechat nebo ne
            end = end + 200  
        
        i = i + 1
    
    # 0 pokud to do konce nenajde    
    return 0  
    

def main(publicKey):
    Q = literal_eval(publicKey)
    print(findPrivate(Q))

if __name__ == '__main__':
    main(sys.argv[1])