from Domain.vanzare import getPret, getGen_carte, getTitlu_carte, creeazaVanzare
from Logic.CRUD import adaugareVanzare
from Logic.functionalitati import discount, modificare_gen, pretMinimGen, ordonare, nrTitluriDistincte, undo, redo, \
    l_noua


def testDiscount():
    lista = []
    lista = adaugareVanzare("1", "Ion", "Drama", 30, "none", lista)
    lista = adaugareVanzare("2", "Poezii", "literatura", 27, "gold", lista)
    lista = adaugareVanzare("3", "Teatru", "literatura", 60, "silver", lista)
    lista_cu_reducere = discount(lista)
    assert len(lista) == len(lista_cu_reducere)
    assert getPret(lista_cu_reducere[1]) == 24.3
    assert getPret(lista_cu_reducere[2]) == 57

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
        creeazaVanzare("3", "Teatru", "gen3", 10.5, "gold"),
        creeazaVanzare("4", "titlu4", "gen1", 17, "silver"),
        creeazaVanzare("5", "titlu5", "gen3", 22.99, "none"),
        creeazaVanzare("6", "titlu6", "gen2", 50, "gold")
    ]

def testPretMinimGen():
    lista = getData()
    lista_preturi_minime = pretMinimGen(lista)
    assert lista_preturi_minime[0][1] == 17
    assert lista_preturi_minime[2][1] == 10.5
    assert len(lista_preturi_minime) == 3

    lista_2 = []
    try:
        pretMinimGen(lista_2)
        assert False
    except ValueError:
        assert True

def getData2():
    return [
        creeazaVanzare("1", "Ion", "gen1", 101.8, "silver"),
        creeazaVanzare("2", "Poezii", "gen2", 27, "none"),
        creeazaVanzare("3", "Teatru", "gen1", 10.5, "gold"),
        creeazaVanzare("4", "titlu4", "gen3", 17, "silver")
    ]

def testOrdonare():
    lista =getData2()
    l_ordonata = ordonare(lista)
    assert lista[2] == l_ordonata[0]
    assert lista[1] == l_ordonata[2]
    assert len(lista) == len(l_ordonata)

    lista_2 = []
    try:
        lista_2 = ordonare(lista_2)
        assert False
    except ValueError:
        assert True

def getData3():
    return [
        creeazaVanzare("1", "Ion", "gen1", 30, "silver"),
        creeazaVanzare("2", "Poezii", "gen3", 27, "none"),
        creeazaVanzare("3", "Teatru", "gen1", 10.5, "gold"),
        creeazaVanzare("4", "titlu4", "gen4", 17, "silver"),
        creeazaVanzare("5", "Teatru", "gen1", 22.99, "none"),
        creeazaVanzare("6", "titlu6", "gen2", 50, "gold"),
        creeazaVanzare("7", "titlu7", "gen1", 13.9, "none"),
        creeazaVanzare("8", "Ion", "gen4", 64, "silver"),
        creeazaVanzare("9", "titlu9", "gen2", 11, "gold"),
        creeazaVanzare("10", "titlu5", "gen3", 23.16, "none")
    ]

def testTitluriDistincte():
    lista = getData3()
    lista_titluri_distincte = nrTitluriDistincte(lista)
    assert lista_titluri_distincte[0][1] == 3
    assert len(lista_titluri_distincte) == 4
    assert lista_titluri_distincte[2][1] == 2
    lista2 = []

    try:
        lista_2 = nrTitluriDistincte(lista2)
        assert False
    except ValueError:
        assert True

def testUndoRedo():
    lista = []
    lista_versiuni = [lista]
    versiunea_curenta = 0
    lista = adaugareVanzare('1', 'titlu1', 'gen1', 120, 'silver', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)
    lista = adaugareVanzare('2', 'titlu2', 'gen2', 46, 'none', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)
    lista = adaugareVanzare('3', 'titlu3', 'gen3', 50, 'gold', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)

    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 2
    assert lista[1] == {'id': '2', 'titlu_carte': 'titlu2', 'gen_carte': 'gen2', 'pret': 46, 'tip_reducere_client': 'none'}
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 1
    assert lista[0] == {'id': '1', 'titlu_carte': 'titlu1', 'gen_carte': 'gen1', 'pret': 120, 'tip_reducere_client': 'silver'}
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 0
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 0
    assert lista == []

    lista_versiuni = [[]]
    versiunea_curenta = 0
    lista = adaugareVanzare('1', 'titlu1', 'gen1', 120, 'silver', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)
    lista = adaugareVanzare('2', 'titlu2', 'gen2', 46, 'none', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)
    lista = adaugareVanzare('3', 'titlu3', 'gen3', 50, 'gold', lista)
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)


    lista, versiunea_curenta = redo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 3
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 1
    lista = adaugareVanzare('4', 'titlu4', 'gen4', 40, 'gold', lista)
    assert len(lista) == 2
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista)
    lista, versiunea_curenta = redo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 2
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 1
    assert lista[0] == {'id': '1', 'titlu_carte': 'titlu1', 'gen_carte': 'gen1', 'pret': 120, 'tip_reducere_client': 'silver'}
    lista, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 0
    lista, versiunea_curenta = redo(lista_versiuni, versiunea_curenta)
    lista, versiunea_curenta = redo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 2
    assert lista[0] == {'id': '1', 'titlu_carte': 'titlu1', 'gen_carte': 'gen1', 'pret': 120, 'tip_reducere_client': 'silver'}
    assert lista[1] == {'id': '4', 'titlu_carte': 'titlu4', 'gen_carte': 'gen4', 'pret': 40, 'tip_reducere_client': 'gold'}
    lista, versiunea_curenta = redo(lista_versiuni, versiunea_curenta)
    assert len(lista) == 2

    lista_vanzari = []
    versiunea_curenta = 0
    lista_vanzari = adaugareVanzare('1', 'titlu1', 'gen1', 35, 'silver', lista_vanzari)
    lista_vanzari = adaugareVanzare('2', 'titlu2', 'gen2', 100, 'silver', lista_vanzari)
    lista_vanzari = adaugareVanzare('3', 'titlu3', 'gen1', 25, 'none', lista_vanzari)
    lista_versiuni = [lista_vanzari]

    lista_vanzari = discount(lista_vanzari)
    assert getPret(lista_vanzari[1]) == 95
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista_vanzari)
    lista_vanzari, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert getPret(lista_vanzari[1]) == 100

    lista_vanzari = modificare_gen(lista_vanzari, '2', 'titlu2', 'gen1')
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista_vanzari)
    assert getGen_carte(lista_vanzari[1]) == 'gen1'
    lista_vanzari, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert getGen_carte(lista_vanzari[1]) == 'gen2'

    lista_vanzari = ordonare(lista_vanzari)
    assert getPret(lista_vanzari[0]) == 25
    lista_versiuni, versiunea_curenta = l_noua(lista_versiuni, versiunea_curenta, lista_vanzari)
    lista_vanzari, versiunea_curenta = undo(lista_versiuni, versiunea_curenta)
    assert getPret(lista_vanzari[0]) == 35
