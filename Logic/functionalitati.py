from Domain.vanzare import getTip_reducere_client, getPret, creeazaVanzare, getId, getTitlu_carte, getGen_carte
from Logic.CRUD import cautare, actualizare


def discount(lista):
    if len(lista) == 0:
        raise ValueError("Lista de carti nu poate fi goala")
    lista_noua = []
    for vanzare in lista:
        if getTip_reducere_client(vanzare) == 'silver':
            pret = getPret(vanzare) * (100 - 5)/100
            vanzare_noua = creeazaVanzare(getId(vanzare), getTitlu_carte(vanzare), getGen_carte(vanzare), pret, getTip_reducere_client(vanzare))
            lista_noua.append(vanzare_noua)

        elif getTip_reducere_client(vanzare) == 'gold':
            pret = getPret(vanzare) * (100 - 10) / 100
            vanzare_noua = creeazaVanzare(getId(vanzare), getTitlu_carte(vanzare), getGen_carte(vanzare), pret, getTip_reducere_client(vanzare))
            lista_noua.append(vanzare_noua)

        else:
            lista_noua.append(vanzare)

    return lista_noua

def modificare_gen(lista, id_carte, titlu_carte, gen_carte):
    '''
    Modificarea genului pentru un titlu dat
    :param lista: lista intiala
    :param id_carte: id-ul cartii
    :param titlu_carte: titlul cartii
    :param gen_carte: genul cartii
    :return: lista modificata
    '''
    if gen_carte == '' or titlu_carte == '':
        raise ValueError("genul sau titlul nu pot fi texte goale")

    vanzare = cautare(lista, id_carte)
    if vanzare == None:
        raise ValueError("Id-ul trebuie sa existe in lista")

    vanzare_noua = creeazaVanzare(id_carte, titlu_carte, gen_carte, getPret(vanzare), getTip_reducere_client(vanzare))
    lista_modificata = actualizare(lista, vanzare_noua)
    return  lista_modificata

def pretMinimGen(lista):
    '''
    determina pretul minim pentru fiecare gen
    :param lista: lista de vanzari
    :return: o lista de tupluri, care contine un gen din lista si pretul minim pentru acest gen
    '''
    if len(lista) == 0:
        raise ValueError("Lista nu poate fi goala")

    l_genuri = []
    for vanzare in lista:
        if getGen_carte(vanzare) not in l_genuri:
            l_genuri.append(getGen_carte(vanzare))

    l_preturi_min = []

    for gen in l_genuri:
        pret_min = getPret(lista[0])
        for vanzare in lista:
            if getGen_carte(vanzare) == gen:
                if pret_min >= getPret(vanzare):
                    pret_min = getPret(vanzare)
        l_preturi_min.append(pret_min)

    return l_preturi_min

def ordonare(lista):
    '''
    Ordoneza o lista de vanzari crescator dupa pret
    :param lista: lista de vanzari intiala
    :return: lista ordonata
    '''
    if len(lista) == 0:
        raise ValueError("Lista de vanzari nu poate fi goala")

    return sorted(lista, key=getPret)

def nrTitluriDistincte(lista_vanzari):
    '''
    creeaza o lista cu titlurile distincte din lista de vanzari
    :param lista_vanzari: lista de vanzari
    :return: numarul de titluri distincte si o lista cu acele titluri
    '''

    if len(lista_vanzari) == 0:
        raise ValueError('Lista nu poate fi goala')

    lista_genuri = []
    lista_titluri_distincte = []

    for vanzare in lista_vanzari:
        if getGen_carte(vanzare) not in lista_genuri:
            lista_genuri.append(getGen_carte(vanzare))

    for gen in lista_genuri:
        lista_titluri = []
        for vanzare in lista_vanzari:
            if getGen_carte(vanzare) == gen:
                titlu_carte = getTitlu_carte(vanzare)
                ok = True
                i = 0
                while ok == True and i <= len(lista_titluri) - 1:
                    if titlu_carte == lista_titluri[i]:
                        ok = False
                    else:
                        i += 1

                if ok == True:
                    lista_titluri.append(titlu_carte)
        lista_titluri_distincte.append((gen, len(lista_titluri)))

    return lista_titluri_distincte

def undo(lista_versiuni, versiune_curenta):
    '''
    sterge ultima operatiune facuta
    :param lista_versiuni: lista de versiuni anterioare
    :param versiune_curenta: versiunea la care ma aflu
    :return: versiunea de pe pozitia versiune_curenta-1 din lista de versiuni
    '''
    if versiune_curenta == 0 and lista_versiuni[0] == []:
        return [], 0
    elif versiune_curenta == 0 and lista_versiuni[0] != []:
        return lista_versiuni[0], versiune_curenta

    versiune_curenta = versiune_curenta - 1
    return lista_versiuni[versiune_curenta], versiune_curenta

def redo(lista_versiuni, versiune_curenta):
    '''
    revine la operatiunea de dinaintea stergerii.
    :param lista_versiuni: lista de versiuni anterioare
    :param versiune_curenta: versiunea curenta la care ma aflu
    :return: versiunea de pe pozitia versiune_curenta+1 din lista de versiuni
    '''

    if versiune_curenta != len(lista_versiuni) - 1:
        versiune_curenta = versiune_curenta + 1
        return lista_versiuni[versiune_curenta], versiune_curenta
    else:
        return lista_versiuni[versiune_curenta], versiune_curenta

def l_noua(lista_versiuni, versiunea_curenta, lista_vanzari):
    '''
    Adauga la o lista de versiuni o lista noua.
    :param lista_versiuni: lista de versiuni anterioare
    :param versiunea_curenta: versiunea curenta
    :param lista_vanzari: lista de vanzari pe care o adaug la lista de versiuni
    :return: lista de versiuni in urma adaugarii lista_versiuni si versiune_curenta
    '''

    while versiunea_curenta < len(lista_versiuni)-1:
        lista_versiuni.pop()

    lista_versiuni.append(lista_vanzari)
    versiunea_curenta = versiunea_curenta + 1
    return lista_versiuni, versiunea_curenta