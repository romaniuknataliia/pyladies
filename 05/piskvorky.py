herni_pole = '--------------------'

print('Budes hrat symbolem "x" a pocitac symbolem "o"!')

hrac_hraje_symbolem = 'x'
pocitac_hraje_symbolem = 'o'

'''def pocitac_hraje_symbolem(symbol_hrace):
    while (symbol_hrace != 'x') or (symbol_hrace != 'o'):
        if symbol_hrace == 'x':
            symbol_pocitace = 'o'
            return symbol_pocitace
            break
        elif symbol_hrace == 'o':
            symbol_pocitace = 'x'
            return symbol_pocitace
        else:
            symbol_hrace = input('Vyber si "x" nebo "o": ')
'''
#commit info
def vyhodnot(herni_pole):
    if 'xxx' in herni_pole:
        return 'x'
    elif 'ooo' in herni_pole:
        return 'o'
    elif '-' not in herni_pole:
        return '!'
    else:
        return '-'

def tah(herni_pole, cislo_policka, symbol):
    return herni_pole[:cislo_policka - 1] + symbol + herni_pole[pozice:]

def tah_hrace(herni_pole):
    odpoved = input('Na kterou pozici chces hrat? Vyber cislo od 1 do 20: ')
    try:
        cislo_policka = int(odpoved)
    except ValueError:
        print('To nebylo číslo!')
    else:
        if 0 < cislo_policka < 21 and herni_pole[cislo_policka - 1] == '-':
            return herni_pole[:cislo_policka - 1] + hrac_hraje_symbolem + herni_pole[cislo_policka:]
        else:
            print('To nedává smysl!')

    '''cislo_policka_dava_smysl = 0 < cislo_policka < 21
    if cislo_policka_dava_smysl and herni_pole[cislo_policka + 1] == '-':
        return herni_pole[:cislo_policka - 1] + hrac_hraje_symbolem + herni_pole[cislo_policka:]
    else:
        print("Bud cislo policka nedava smysl anebo je jiz obsazene")'''


#print('Pocitac hraje symbolem: ', pocitac_hraje_symbolem(input('Hrajes "x" nebo "o"? ')))
#print(vyhodnot(herni_pole))

print(tah_hrace(herni_pole))
