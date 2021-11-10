from Domain.vanzare import getTip_reducere_client, getPret, creeazaVanzare, getId, getTitlu_carte, getGen_carte
from Logic.CRUD import cautare, actualizare


def discount(lista):
    if len(lista) == 0:
        raise ValueError("Lista de carti nu poate fi goala")
    lista_noua = []
    for vanzare in lista:
        if getTip_reducere_client(vanzare) == "silver":
            pret = getPret(vanzare) * (100 - 5)/100
            vanzare_noua = creeazaVanzare(getId(vanzare), getTitlu_carte(vanzare), getGen_carte(vanzare), getPret(vanzare), getTip_reducere_client(vanzare))
            lista_noua.append(vanzare_noua)

        elif getTip_reducere_client(vanzare) == "gold":
            pret = getPret(vanzare) * (100 - 10) / 100
            vanzare_noua = creeazaVanzare(getId(vanzare), getTitlu_carte(vanzare), getGen_carte(vanzare), getPret(vanzare), getTip_reducere_client(vanzare))
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
        for vanzare in lista:
            if getGen_carte(vanzare) == gen:
                pret_min = getPret(vanzare)
                break

    for vanzare in lista:
        if (getGen_carte(vanzare) == gen) and (getPret(vanzare) < pret_min):
            pret_min = getPret(vanzare)

    l_preturi_min.append(gen, pret_min)

    return l_preturi_min
