from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificaVanzare
from Logic.functionalitati import discount, modificare_gen, pretMinimGen, ordonare, nrTitluriDistincte, redo, undo


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicarea discount-ului(5% pentru reducerile silver si 10% pentru reducerile gold)")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7.Ordonarea unei liste de vanzari crescator dupa pret")
    print("8.Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u.Tasta pentru undo")
    print("r.Tasta pentru redo")
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


def uiPretMinimGen(l):
    try:
        l_pret_min = pretMinimGen(l)
        for pret in l_pret_min:
            print('Pretul minim pentru genul {pret[0]} este {pret[1]}')
        return l
    except ValueError as ve:
        print("Eroare: ", ve)
    return  l

def uiOrdonare(l):
    try:
        l = ordonare(l)
        showAll(l)
    except ValueError as ve:
        print('Eroare: ', ve)

    return l

def uiTitluriDistincte(lista_vanzari):
    try:
        lista = nrTitluriDistincte(lista_vanzari)
        for tuplu in lista:
            print(f'Numarul de titluri distincte pentru genul {tuplu[0]} este {tuplu[1]}')
    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_vanzari

def uiUndo(lista_versiuni, versiunea_curenta):
    return undo(lista_versiuni, versiunea_curenta)

def uiRedo(lista_versiuni, versiunea_curenta):
    return redo(lista_versiuni, versiunea_curenta)

def runMenu(lista):

    lista_versiuni = [lista]
    versiunea_curenta = 0

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
        elif optiune == "6":
            lista = uiPretMinimGen(lista)
        elif optiune == '7':
            lista = uiOrdonare(lista)
        elif optiune == '8':
            lista = uiTitluriDistincte(lista)
        elif optiune == 'u':
            if versiunea_curenta < 1:
                print('Nu se mai poate face undo')
            else:
                lista, versiune_curenta = uiUndo(lista_versiuni, versiunea_curenta)
                if lista == []:
                    print(f'Lista este goala {lista}')
        elif optiune == 'r':
            if versiunea_curenta == len(lista_versiuni) - 1:
                print('Nu se mai poate face redo')
            else:
                lista, versiunea_curenta = uiRedo(lista_versiuni, versiunea_curenta)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")