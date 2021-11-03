from Domain.vanzare import getId, creeazaVanzare


def adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, l):
    '''
    adauga o vanzare intr-o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param l: lista de vanzari
    :return: o lista continand atat elementele vechi, cat si noua vanzare
    '''
    vanzare  = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    return l + [vanzare]

def stergereVanzare(id, l):
    '''
    sterge o vanzare dupa id  dintr-o lista
    :param id: id-ul unei vanzari de sters, string
    :param l: lista de vanzari
    :return: o lista continand vanzarile cu id-ul diferit de id
    '''
    return [vanzare for vanzare in l if getId(vanzare) != id]

def modificaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, l):
    '''
    modifica o vanzare cu id-ul dat
    :param id: id-ul vanzarii
    :param titlu_carte: titlul unei carti
    :param gen_carte: genul unei carti
    :param pret: pretul unei carti
    :param tip_reducere_client: poate fi: none, silver, sau gold
    :param l: lista de vanzari
    :return: lista modificata
    '''
    listaNoua = []
    for vanzare in l:
        if getId(vanzare) == id:
            vanzareNoua = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def getById(id, l):
    '''
    gaseste o vanzare cu id-ul dat intr-o lista
    :param id: string
    :param l: lista de vanzari
    :return: vanzare cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for vanzare in l:
        if getId(vanzare) == id:
            return vanzare
    return None

def cautare(lista, id_carte):
    '''
    citeste o carte din lista de vanzari
    :param lista: lista de carti
    :param id_carte: id-ul cartii
    :return: cartea cautata daca aceasta exista in lista
    '''
    carte_id = None
    for vanzare in lista:
        if getId(vanzare) == id_carte:
            carte_id = vanzare

    if carte_id:
        return carte_id
    else:
        return None

def actualizare(lista, vanzare_noua):
    '''
    actualizeaza o vanzare din lista
    :param lista: lista  initiala
    :param vanzare_noua: vvanzarea pe care o actualizam
    :return: lista actualizata
    '''
    lista_noua = []
    for vanzare in lista:
        if getId(vanzare) == getId(vanzare_noua):
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua