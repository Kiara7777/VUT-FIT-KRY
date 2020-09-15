# VUT FIT KRY

Projekty do předmětu Kryptografie na VUT FIT 4. semestr, zima, magisterské studium

## Projekt 1
Dostali jste několik souborů které jsou šifrovány neznámou synchronní proudovou šifrou. Vašim cílem je zjistit tajemství, které má formát KRY{24 znaků ASCII textu}.

Programovací jazyk je Python 3. Odevzdvávejte archiv xlogin00.zip. Archiv bude obsahovat solution.py (soubor s obsahem ručního řešení), solution_sat.py (soubor s obsahem sat řešení), doc.pdf (dokumentace) a volitelně install.sh (pro automatickou instalaci závislostí, pouze pomocí pip3, pouze pro SAT řešení, z3 bude již nainstalován). Skripty po spuštění vypíší na stdout tajemství. Skripty budou pracovat s jedním argumentem. Argument bude cílová cesta k adresáři ve které bude rozbalený obsah archivu zadání (neodevzdávejte) a bude zjišťovat tajemství ze souborů v této složce. Pokud skript potřebuje závislosti, musí si je automaticky doinstalovat pomocí install.sh (install.sh bude spuštěn před spuštěním testu). Program vypíše tajemství na stdout a skončí. Vaše řešení bude testováno na Ubuntu 18.04 LTS.

V druhé části zadaní získejte tajemství pomocí SAT solveru aplikovaného na spravnou část šifry. https://www.cs.cornell.edu/gomes/pdf/2008_gomes_knowledge_satisfiability.pdf https://yurichev.com/writings/SAT_SMT_draft-EN.pdf

**SAT neděláno**

## Projekt 2

Vaším úkolem je v libovolném jazyce implementovat program, který bude schopný ze zadaného veřejného ECC klíče vygenerovat klíč privátní. Tento program musí být spustitelný na serveru Merlin.

Dokumentaci není v tomto projektu třeba řešit. Taktéž ošetřování vstupu není předmětem projektu a není tedy nezbytné ošetřovat nevalidní vstupy.

### Vstupní údaje pro ECC

- Fp
```
    0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
```
- a
```
    -0x3
```
- b
```
    0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
```
 - základní bod
 ```
    (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
    0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
```
### Odevzdání projektu
Archiv bude v kořenovém adresáři (bez zanoření) obsahovat Vaše zdrojové soubory a soubor Makefile. Soubor Makefile bude obsahovat pravidlo decipher s parametrem publicKey, kdy na standardním výstupu lze po zavolání očekávat pouze číslo, které je řešením (soukromým klíčem). V případě nedokončeného řešení vypište na standardní výstup 0.
