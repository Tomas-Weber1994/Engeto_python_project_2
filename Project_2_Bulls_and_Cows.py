import random

# Program pozdraví užitele a vypíše úvodní text
def hra():
    statistika_pokusu = []
    oddelovac = "="*50
    print("Ahoj!".center(len(oddelovac)), oddelovac, sep = "\n")
    while True:                                                 # První while cyklus slouží pouze pro případné opakování hry.
        print("Vygeneroval jsem pro tebe náhodné čtyřmístné číslo.".center(len(oddelovac)),
              "Zahrajeme si hru bulls and cows!".center(len(oddelovac)), oddelovac, sep="\n")
        nahodne_cislo = random.choice(seznam_platnych_cisel(1000,10000)) # Vygenerování náhodného čísla splňující parametry hry.
        pocet_pokusu = 0                                         # Počáteční stav, za každé hádání přičteme pokus pro účely případné statistiky
        # print(nahodne_cislo) # Slouží pouze pro testování
        while True:
            hadani = input("Zadej číslo: ")
            print(oddelovac)
            pocet_pokusu += 1
            if je_hadane_cislo_neplatne(hadani) != False: #      # Pokud je číslo neplatné, vytiskne se oznámení o chybě + zadáváme nové číslo
                print(je_hadane_cislo_neplatne(hadani), oddelovac, sep = "\n")
                continue
            if int(hadani) == nahodne_cislo:          # Ověření uhodnutí čísla
                print(f"Správně, uhodl jsi číslo! Zabralo ti to celkem {pocet_pokusu} pokusů.", oddelovac, sep = "\n")
                break
            else:
                # Přiřazení vrácených hodnot z funkcí pro tisk oznámení cows bulls
                bulls, cows = bulls_cows(hadani, nahodne_cislo)[0], bulls_cows(hadani, nahodne_cislo)[1]
                jednotne_mnozne = jednotne_vs_mnozne_cislo_bulls_cows(hadani, nahodne_cislo)
                # Tisk počtu bulls a cows
                print(bulls, jednotne_mnozne[0])
                print(cows, jednotne_mnozne[1])
                print("Hádej dál!", oddelovac, sep = "\n")
        statistika_pokusu.append(pocet_pokusu)   # rozšíření opakované hry a statistika jednotlivých pokusů
        nova_hra = input("Chceš hrát ještě? Pro ukončení programu zadej 'ne': ")
        if nova_hra == "ne":
            vypis_statistiku(pocet_pokusu, statistika_pokusu, oddelovac)
            prumerny_pocet_pokusu = round(sum(statistika_pokusu)/len(statistika_pokusu), 2)
            print("Tvůj průměrný počet pokusů: ", prumerny_pocet_pokusu)
            break
        else:
            print("Spouštím novou hru...", oddelovac, sep = "\n")


def seznam_platnych_cisel(start: int, stop: int): #  Vygeneruje Seznam platných čísel pro hru v daném rozsahu za pomocí funkce
                                                  # , která ověřuje unikátnost jednotlivých číslic
    return [cislo_v_seznamu for cislo_v_seznamu in range(start, stop) if je_unikatni_cislo(cislo_v_seznamu)]

def je_unikatni_cislo(cislo): # Pomocná funkce ověřující unikátnost číslic v čísle
    for cislice in str(cislo):
        if str(cislo).count(str(cislice)) != 1:
            return False
            break
        else:
            continue
    else: return True

def je_hadane_cislo_neplatne(hadani): # Ověření, zda uživatelem zadané číslo je platné.
    if not hadani.isnumeric():
        oznameni = "Toto není číslo!"
        return oznameni
    elif len(hadani) != 4:
        oznameni = "Je potřeba zadat čtyřciferné číslo!"
        return oznameni
    elif hadani.startswith("0"):
        oznameni = "Číslo nesmí začínat nulou!"
        return oznameni
    elif int(hadani) not in seznam_platnych_cisel(1000,10000):
        oznameni = "Jednotlivé číslice se nesmí opakovat!"
        return oznameni
    else:
        return False

def bulls_cows(hadani, nahodne_cislo): # Funkce zjistí počet bulls a cows a vrátí odpovídající oznámení
    cislice_v_hadani = [cislice for cislice in hadani]
    cislice_v_nahodnem_cisle = [cislice for cislice in str(nahodne_cislo)]
    cows = 0
    bulls = 0
    for cisla in range(0,4):
        if cislice_v_hadani[cisla] == cislice_v_nahodnem_cisle[cisla]:
            bulls += 1
        elif cislice_v_hadani[cisla] in cislice_v_nahodnem_cisle and cislice_v_hadani[cisla] != cislice_v_nahodnem_cisle[cisla]:
            cows += 1
    return bulls, cows

def jednotne_vs_mnozne_cislo_bulls_cows(hadani, nahodne_cislo):    # Pomocná funkce k tisku stringu v množném / jednotném čísle
    if bulls_cows(hadani, nahodne_cislo)[0] == 1 and bulls_cows(hadani, nahodne_cislo)[1] == 1:
        oznameni = ["bull", "cow"]
    elif bulls_cows(hadani, nahodne_cislo)[0] == 1:
        oznameni = ["bull", "cows"]
    elif bulls_cows(hadani, nahodne_cislo)[1] == 1:
        oznameni = ["bulls", "cow"]
    else:
        oznameni = ["bulls", "cows"]
    return oznameni

def vypis_statistiku(pocet_pokusu, statistika_pokusu, oddelovac):
    print(oddelovac)
    hra_cislo, pokus = "Číslo hry", "Tvůj počet pokusů"  # pomocné proměnné sloužící jen k zarovnání tisku
    print(hra_cislo.ljust(20), pokus.rjust(20))
    print("-"*50)
    # print(cislo_hry + 1, statistika_pokusu)
    for cislo_hry, _ in enumerate(range(0, len(statistika_pokusu))):
        print(str(cislo_hry + 1).center(10), str(statistika_pokusu[cislo_hry]).rjust(25))
    print(oddelovac)

hra()