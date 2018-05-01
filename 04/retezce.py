#basen = '''Haló haló!
#Co se stalo?
#Prase kozu potrkalo!'''

print(basen)

#print('n' not in basen)

#print(basen.upper())
#print(basen.lower())
#print(basen.count("a"))

#print("------------------------")

'''def inicialy():
    jmeno = input("Zadej sve jmeno: ")
    prijmeni = input("Zadej sve prijmeni: ")
    a = jmeno[0].upper()
    b = prijmeni[0].upper()
    return a + "." + b + "."

print(inicialy())
'''

'''retezec = 'čokoláda'
print(retezec[:4])
print(retezec[2:5])
print(retezec[-4:])'''

def zamen_pismeno(retezec, pozice, znak):
    return retezec[:pozice - 1] + znak + retezec[pozice:]


print(zamen_pismeno("kava", 3, "l"))
