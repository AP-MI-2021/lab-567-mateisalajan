from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare, modificaVanzare
from Logic.functionalitati import discount, modificare_gen, pretMinimGen, ordonare, nrTitluriDistincte, redo, undo, \
    l_noua


def printMenu():
    print("1. CRUD")
    print("2. Aplicarea discount-ului(5% pentru reducerile silver si 10% pentru reducerile gold)")
    print("3. Modificarea genului pentru un titlu dat")
    print("4. Determinarea prețului minim pentru fiecare gen")
    print("5.Ordonarea unei liste de vanzari crescator dupa pret")
    print("6.Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u.Tasta pentru undo")
    print("r.Tasta pentru redo")
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
            print(f'Pretul minim pentru genul {pret[0]} este {pret[1]}')
        return l
    except ValueError as ve:
        print("Eroare: ", ve)
    return l

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

def uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari):
    return l_noua(lista_versiuni, versiunea_curenta, lista_vanzari)

def uiUndo(lista_versiuni, versiunea_curenta):
    return undo(lista_versiuni, versiunea_curenta)

def uiRedo(lista_versiuni, versiunea_curenta):
    return redo(lista_versiuni, versiunea_curenta)

def uiCrud(lista_vanzari, lista_versiuni, versiunea_curenta):

    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare')
        print('y. Revenire')
        optiune = input('Dati optiune: ')
        if optiune == '1':
            lista_vanzari = uiAdaugaVanzare(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '2':
            lista_vanzari = uiStergeVanzare(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '3':
            lista_vanzari = uiModificaVanzare(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == 'a':
            showAll(lista_vanzari)
        elif optiune == 'y':
            break
        else:
            print('Optiune gresita')

    return lista_vanzari, lista_versiuni, versiunea_curenta

def runUi(lista_vanzari):

    lista_versiuni = [lista_vanzari]
    versiunea_curenta = 0

    while True:
        printMenu()
        optiune = input('Dati optiune: ')
        if optiune == '1':
            lista_vanzari, lista_versiuni, versiunea_curenta = uiCrud(lista_vanzari, lista_versiuni, versiunea_curenta)
        elif optiune == '2':
            lista_vanzari = uiDiscount(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '3':
            lista_vanzari = uiModificare_gen(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '4':
            uiPretMinimGen(lista_vanzari)
        elif optiune == '5':
            lista_vanzari = uiOrdonare(lista_vanzari)
            lista_versiuni, versiunea_curenta = uiListaNoua(lista_versiuni, versiunea_curenta, lista_vanzari)
        elif optiune == '6':
            uiTitluriDistincte(lista_vanzari)
        elif optiune == 'x':
            break
        elif optiune == 'u':
            if versiunea_curenta < 1:
                print('Nu se mai poate face undo')
            else:
                lista_vanzari, versiunea_curenta = uiUndo(lista_versiuni, versiunea_curenta)
                if lista_vanzari == []:
                    print(f'Lista este goala {lista_vanzari}')
        elif optiune == 'r':
            if versiunea_curenta == len(lista_versiuni) - 1:
                print('Nu se mai poate face redo')
            else:
                lista_vanzari, versiunea_curenta = uiRedo(lista_versiuni, versiunea_curenta)
        else:
            print('Optiune invalida')
    return lista_vanzari