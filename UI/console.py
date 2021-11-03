from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificaVanzare
from Logic.functionalitati import discount, modificare_gen


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicarea discount-ului(5% pentru reducerile silver si 10% pentru reducerile gold)")
    print("5. Modificarea genului pentru un titlu dat")
    print("a. Afisare vanzari")
    print("x. Iesire")

def uiAdaugaVanzare(l):
    id = input("Dati id-ul: ")
    titlu_carte = input("Dati titlul cartii: ")
    gen_carte = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    tip_reducere_client = input("Dati tipul de reducere: ")
    return adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, l)

def uiStergeVanzare(l):
    id = input("Dati id-ul vanzarii de sters: ")
    return stergereVanzare(id, l)

def uiModificaVanzare(l):
    id = input("Dati id-ul vanzarii de modificat: ")
    titlu_carte = input("Dati titlul altei cartii: ")
    gen_carte = input("Dati genul altei cartii: ")
    pret = float(input("Dati pretul altei cartii: "))
    tip_reducere_client = input("Dati noul tipul de reducere: ")
    return modificaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, l)

def showAll(l):
    for vanzare in l:
        print(toString(vanzare))

def uiDiscount(l):
    lista_noua = discount(l)
    print("lista actualizata in urma aplicarii reducerii este: ")

    for vanzare in lista_noua:
        print(toString(vanzare))

def uiModificare_gen(l):
    try:
        id_nou = input("Dati id-ul cartii al carui gen doriti sa il modificati: ")
        titlu_nou = input("Dati titlul cartii: ")
        gen_nou = input("Dati genul cartii in care doriti sa il modficati")
        lista_noua = modificare_gen(l, id_nou, titlu_nou, gen_nou)
        for vanzare in lista_noua:
            print(toString(vanzare))

    except ValueError as ve:
        print("Eroare: ", ve)
    return l

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista)
        elif optiune == "2":
            lista = uiStergeVanzare(lista)
        elif optiune == "3":
            lista = uiModificaVanzare(lista)
        elif optiune == "4":
            lista = uiDiscount(lista)
        elif optiune == "5":
            lista = uiModificare_gen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")