#!/usr/bin/env python
# Tämä on aloitusskripti

import henkilö
import vuodet

# dictionary - sanakirja

henkilötiedot = [
{"nimi": "aliisa", "syntymävuosi": 1980},
{"nimi":"bob", "syntymävuosi": 1967},
{"nimi": "Cecilia", "syntymävuosi": 1920},
]

henkilöiden_lempivärit = {
    "aliisa": "musta",
    "Bob": "sininen", 
}

henkilöiden_lemmikit = {
    "aliisa": ["Musti"],
    "bob": ["Tupu", "Hupu", "Lupu"],
}

def henkilölistaus():
    henkilöt = []
    for ht in henkilötiedot:
        h = henkilö.Henkilö(ht["nimi"], ht["syntymävuosi"])
        henkilöt.append(h)
    for h in henkilöt:
        print(f"{h.nimi} (s.{h.syntymävuosis})")
        print(f"{h.nimi}, on {h.ikä()}, vuotta vanha.")
        lemmikit = henkilöiden_lemmikit.get(h.nimi, [])
        if lemmikit:
            for lemmikki in lemmikit:
                print("Lemmikki:", lemmikki)
            try:
                print("Lempiväri:", henkilöiden_lempivärit[h.nimi])
            except KeyError:
                print("Ei lempiväriä tiedossa")
                print("-")
        if h.ikä() > 18:
            print("Täysi-ikäinen")
        if h.ikä() < 50:
            print("nuori vielä")    
henkilölistaus()



def pääfunktio():
    syntymävuosi = 1970
    aliisa = henkilö.Henkilö("Aliisa", 1980)
    bob = henkilö.Henkilö(nimi="Bob", syntymävuosi=1967)
    henkilöt = [aliisa, bob]



#pääfunktio()

# teksti = input("Anna luku: ")  # input on funktio

# print(teksti)  # "print" on siis funktio



# if teksti.isdigit():  # isdigit = str luokan metodi (method of str class)
#     luku = int(teksti)
# elif teksti == "yksi":
#     luku = 1
# elif teksti == "kaksi":
#     luku = 2
# elif teksti == "kymppi":
#     luku = 10
# else:
#     print("Ei ollu luku. Varmaan 0 käy sitten.")
#     luku = 0

# print("Luku on:", luku)

# if luku > 10:
#     print("suurempi kuin 10")
# elif luku == 10:
#     print("tasan 10")
# else:
#     print("pienempi kuin 10")
