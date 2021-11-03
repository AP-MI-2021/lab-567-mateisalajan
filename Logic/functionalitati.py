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