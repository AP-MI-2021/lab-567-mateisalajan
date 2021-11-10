from Domain.vanzare import getPret, getGen_carte, getTitlu_carte, creeazaVanzare
from Logic.CRUD import adaugareVanzare
from Logic.functionalitati import discount, modificare_gen, pretMinimGen


def testDiscount():
    lista = []
    lista = adaugareVanzare("1", "Ion", "Drama", 30, "none", lista)
    lista = adaugareVanzare("2", "Poezii", "literatura", 27, "none", lista)
    lista = adaugareVanzare("3", "Teatru", "literatura", 32, "none", lista)
    lista_cu_reducere = discount(lista)
    assert len(lista) == len(lista_cu_reducere)
    assert getPret(lista_cu_reducere[0]) == 30
    assert getPret(lista_cu_reducere[2]) == 32

    lista2 = []
    try:
        discount(lista2)
        assert False
    except ValueError:
        assert True

def testModificare_gen():
    lista = []
    lista = adaugareVanzare("1", "Ion", "drama", 30, "silver", lista)
    lista = adaugareVanzare("2", "Poezii", "pastel", 27, "none", lista)
    lista = adaugareVanzare("3", "Teatru", "literatura", 32, "none", lista)
    id = "2"
    titlu = "Poezii"
    gen = "literatura"
    lista_noua = modificare_gen(lista, id, titlu, gen)
    assert len(lista) == len(lista_noua)
    assert getGen_carte(lista_noua[1]) == "literatura"
    assert getGen_carte(lista[1]) != getGen_carte(lista_noua[1])
    assert getTitlu_carte(lista[1]) == getTitlu_carte(lista_noua[1])
    id2 = "10"
    titlu2 = "Ion"
    gen2 = "drama"
    try:
        modificare_gen(lista, id2, titlu2, gen2)
        assert False
    except ValueError:
        assert True

def getData():
    return [
        creeazaVanzare("1", "Ion", "gen1", 30, "silver"),
        creeazaVanzare("2", "Poezii", "gen2", 27, "none"),
        creeazaVanzare("3", "Teatru", "gen1", 10.5, "gold"),
        creeazaVanzare("4", "titlu4", "gen3", 17, "silver"),
        creeazaVanzare("5", "titlu5", "gen3", 22.99, "none"),
        creeazaVanzare("6", "titlu6", "gen2", 50, "gold")
    ]

def testPretMinimGen():
    lista = getData()
    l_preturi_min = pretMinimGen(lista)
    assert len(l_preturi_min) == 3
    assert l_preturi_min[0] == 10.5
    assert l_preturi_min[1] == 27

    lista_2 = []
    try:
        pretMinimGen(lista_2)
        assert  False
    except ValueError:
        assert True