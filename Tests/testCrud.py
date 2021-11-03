from Domain.vanzare import getId, getTitlu_carte, getGen_carte, getPret, getTip_reducere_client
from Logic.CRUD import adaugareVanzare, getById, stergereVanzare, modificaVanzare


def testAdaugaVanzare():
    lista = []
    lista = adaugareVanzare("1", "Ion", "literatura", 10, "silver", lista)
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu_carte(getById("1", lista)) == "Ion"
    assert getGen_carte(getById("1", lista)) == "literatura"
    assert getPret(getById("1", lista)) == 10
    assert getTip_reducere_client(getById("1", lista)) == "silver"

def testStergePrajitura():
    lista = adaugareVanzare("1", "Ion", "literatura", 10, "silver", [])
    lista = adaugareVanzare("2", "Poezii", "literatura", 10, "silver", lista)

    lista = stergereVanzare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None

    lista = stergereVanzare("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaVanzare():
    lista = []
    lista = adaugareVanzare("1", "Ion", "literatura", 10, "silver", [])
    lista = adaugareVanzare("2", "Poezii", "literatura", 10, "silver", lista)

    lista = modificaVanzare("1", "Teatru", "literatura", 32, "none", lista)

    vanzareUpdatata = getById("1", lista)
    assert getId(vanzareUpdatata) == "1"
    assert getTitlu_carte(vanzareUpdatata) == "Teatru"
    assert getGen_carte(vanzareUpdatata) == "literatura"
    assert getPret(vanzareUpdatata) == 32
    assert getTip_reducere_client(vanzareUpdatata) == "none"

    vanzareNeupdatata = getById("2", lista)
    assert getId(vanzareNeupdatata) == "2"
    assert getTitlu_carte(vanzareNeupdatata) == "Poezii"
    assert getGen_carte(vanzareNeupdatata) == "literatura"
    assert getPret(vanzareNeupdatata) == 10
    assert getTip_reducere_client(vanzareNeupdatata) == "silver"

    lista = []
    lista = adaugareVanzare("1", "Ion", "literatura", 10, "silver", [])

    lista = modificaVanzare("3", "Teatru", "literatura", 32, "none", lista)
    vanzareNeupdatata = getById("1", lista)
    assert getId(vanzareNeupdatata) == "1"
    assert getTitlu_carte(vanzareNeupdatata) == "Ion"
    assert getGen_carte(vanzareNeupdatata) == "literatura"
    assert getPret(vanzareNeupdatata) == 10
    assert getTip_reducere_client(vanzareNeupdatata) == "silver"