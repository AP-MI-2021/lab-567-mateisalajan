def creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''
    creeaza o vanzare
    :param id: id-ul unei vanzari
    :param titlu_carte: tittlul unei carti
    :param gen_carte: genul unei carti
    :param pret:pretul unei carti
    :param tip_reducere_client: poate fi: none, silver, sau gold
    :return: un dictionar ce retine o vanzare
    '''
    return {
        'id': id,
        'titlu_carte': titlu_carte,
        'gen_carte': gen_carte,
        'pret': pret,
        'tip_reducere_client': tip_reducere_client
    }

def getId(vanzare):
    '''
    ia id-ul vanzarii
    :param vanzare: un dictionar de tip vanzare
    :return: id-ul vanzarii
    '''
    return vanzare['id']

def getTitlu_carte(vanzare):
    '''
    ia titlul unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: titlul unei carti
    '''
    return vanzare['titlu_carte']

def getGen_carte(vanzare):
    '''
    ia genul unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: genul unei carti
    '''
    return vanzare['gen_carte']

def getPret(vanzare):
    '''
    ia pretul unei carti
    :param vanzare: un dictionar de tip vanzare
    :return: pretul unei carti
    '''
    return vanzare['pret']

def getTip_reducere_client(vanzare):
    '''
    ia tipul de reducere a unui client,acesta poate fi none, silver, sau gold
    :param vanzare: un dictionar de tip vanzare
    :return: tipul de reducere a unui client
    '''
    return vanzare['tip_reducere_client']

def toString(vanzare):
    return "id: {}, titlu_carte: {}, gen_carte: {}, pret: {}, tip_reducere_client: {}".format(
        getId(vanzare),
        getTitlu_carte(vanzare),
        getGen_carte(vanzare),
        getPret(vanzare),
        getTip_reducere_client(vanzare)
    )