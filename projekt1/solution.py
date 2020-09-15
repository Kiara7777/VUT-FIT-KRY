#----------------------------------------------
# Projekt 1 do predmetu Kryptografie, VUT FIT
# Kryptoanalyza a vyuziti SAT solveru
# Sara Skutova, xskuto00@stud.fit.vutbr.cz
# 14.3.2019
#----------------------------------------------
import argparse
import os
import sys


SUB = [0, 1, 1, 0, 1, 0, 1, 0]
N_B = 32
N = 8 * N_B

sub0 = ['000', '011', '101', '111']
sub1 = ['001', '010', '100', '110']


# Next keystream
def step(x):
    x = (x & 1) << N+1 | x << 1 | x >> N-1

    y = 0
    for i in range(N):
        y |= SUB[(x >> i) & 7] << i
    return y


#provede reverzaci prvni casti funkce step
#vrati puvodni x, ktere vstuje do fukce step
def shiftX(x):
    #je to ve formatu string, nezapomen na to
    #puvodni pridava 2 prvky, posledni a prvni, takze bude mit velikost 258, pokud se tam na zacatek neprida 0
    
    #poseldni bude nula, mela by byt
    #prvni je 0 nebo 1 podle toho co bylo puvodne nakoci
    
    #zbavit se posledniho
    strShift = x[:-1]
    
    #puvodni pridava o 2 prvky navic, posledni a prvni, posledniho jsem se zbavili, 
    
    if (len(strShift) > 256): #na zacatek se pridala 1, musime se toho zbavit
        strShift = strShift[1:]
    
    #mensi uprava pro odstraneni prebytecnych nul na zacatku, potrebuju uchovat nuly jenom na konci - NEFUNGUJE, NEPOUZIVAT!!!!!
    #test = int(strShift, 2)
    #testL = len(bin(test)) - 2
    #if (testL < 256):
    #    strShift = str(bin(test))[2:]
    
    return strShift

#z pole moznych vysledku vybere takove ktere da spravny vysledek z funkce step
def mainX(pole, puvodniX):
    

    puvodniX = puvodniX[::-1]
    
    puvodniX = int(puvodniX, 2)
    
    vybraneX = 0
    
    for item in pole:
        x = int(item, 2)
        newX = step(x)
        
        if (puvodniX == newX):
            vybraneX = item
            break
        
    return vybraneX
    
    
    
def nextbit(current, bit):
    last2 = current[-2:] #posledni 2 stare sekvence
    first2 = "" # prvni 2 ze sekvence, ze ktere budu pridavat poseldni prvek ke stare sekvenci
    
    novy = ""
    
    nalezeno = ""
    last = ""
    
    if (bit == '0'):
        for i in sub0:
            first2 = i[:2]
            if (last2 == first2):
                last= i[-1:]
                novy = current + last
                nalezeno = i
                break
    else:
        for i in sub1:
            first2 = i[:2]
            if (last2 == first2):
                last = i[-1:]
                novy = current + last
                nalezeno = i
                break
    
    return novy            
            
    
    

#reverzace funkcec step
#prvni verze, ktera se spusti na zacatku
#X JE STRING BITU!!!!
def reverseStep(x, inic):
    
    pocet = len(x)
    pole = []
    
    puvodniX = x
    
    for i in range(pocet): # projit pres vsechny bity vstupu
        bit = x[-1:] 
        if (inic == 0): #prvni iterace, musim vytvorit nove startovaci klice
            if (bit == '0'):
                pole = sub0.copy()
            else:
                pole = sub1.copy()     
        else:
            for (index, item) in enumerate(pole):
                pole[index] = nextbit(item, bit)
                
            
        x = x[:-1]
        inic += 1
    
    for (index, item) in enumerate(pole):
        pole[index] = shiftX(item)
    
    vybraneX = mainX(pole, puvodniX)
    
    return vybraneX


#zpracova prikazouvou radku, ziska adresar ve kterem jsou soubory
def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help = "Adresar ze kterem se nachazi zasifrovane soubory")
    args = parser.parse_args()
    
    return args.dir

#zkontroluje zda se jedna o adresar
def isDire(directory):
    if (os.path.isdir(directory)):
        return True
    else:
        return False
    
#cte zadany soubor a vrati obsah jako byty
def readFile(file):
    with open(file, "rb") as binary_file:
        text = binary_file.read()
    
    bArray = bytearray(text)
    return bArray

#prevede bytove pole do jedineho stringu, zachovava cely pocet bitu na byte - tj. na zacatku posloupnosti budou i nuly
def bytes2string(pole):
    string = ""
    for byte in pole:
        string += format(byte, '08b')

    return string

#transformuje string bitu na vystupni string
def sBit2String(bits):
    #string -> int -> byte -> string
    bits = bits[::-1]
    hInt = int(bits, 2)
    hByte = hInt.to_bytes(N_B, byteorder='little')
    
    hString = hByte.decode('ascii')
    hString = hString.rstrip('\x00')
    
    
    return hString
    
    


#desifrovani
#zasifrovany XOR normalni = klic
#zasifrovany xor klic = normalni
#normali xor klic = zasifrovany
def decryption1(enc, normal, size):
    
    key = bytearray(size)
    
    for i in range(size):
        key[i] = enc[i] ^ normal[i]
        
    return key
        
                
def main():
    directory = getArg()
    ok = isDire(directory)
    
    if (not ok):
        sys.exit("Zadany argument: " + directory + ", neni adresar")
    
    bisTxt = "text"
    bisTxtEc = "text"
    
    hintGif = "text"
    superPy = "test"
        
    if (directory.endswith("/")):
        bisTxt = directory + "bis.txt"
        bisTxtEc = directory + "bis.txt.enc"
        hintGif = directory + "hint.gif.enc"
        superPy = directory + "super_cipher.py.enc"
    else:
        bisTxt = directory + "/bis.txt"
        bisTxtEc = directory + "/bis.txt.enc"
        hintGif = directory + "/hint.gif.enc"
        superPy = directory + "/super_cipher.py.enc"
    
    bis = readFile(bisTxt)
    encBis = readFile(bisTxtEc)
    
    encHint = readFile(hintGif)
    encSuper = readFile(superPy)
    
    
    key = decryption1(encBis, bis, len(bis))
    
    #print(key[32:65])
    
    # prvni keystream, ktery se vygeneruje
    initKey = key[:N_B]
    
    
    #prevraceni keystreamu a ulozeni jako int
    keystr = int.from_bytes(initKey,'little')
    keystr = keystr.to_bytes(32, byteorder='big')
    
    keystr = bytes2string(keystr)
    
    keystr = keystr[::-1]

    #cast prevzateho kodu
    for i in range(N//2):
        keystr = reverseStep(keystr, 0)
        keystr = keystr[::-1]
    
    
    konec = sBit2String(keystr)
    
    sys.stdout.write(konec)
    
    #KRY{xskuto00-d67d7b42e0a3c96}
    #super = decryption1(encSuper, key, len(key))
    
    #######################################################
    
    #keystr = int.from_bytes("KRY{xskuto00-d67d7b42e0a3c96}".encode(),'little')
    
    #for i in range(N//2):
    #    keystr = step(keystr)
        
    #keystr2 = step(keystr)
    
    #print(hex(keystr2))
    
    #keystr3 = step(keystr2)
    
    #super = decryption1(encSuper, encHint, len(encSuper))
    
    #print(super)

    
    
    
    
    
    
        
    

if __name__ == '__main__':
    main()