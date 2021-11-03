from Domain.vanzare import creeazaVanzare, getId, getTitlu_carte, getGen_carte, getPret, getTip_reducere_client


def testVanzare():
    vanzare = creeazaVanzare("1", "Ion", "literatura", 10, "silver")
    assert getId(vanzare) == "1"
    assert getTitlu_carte(vanzare) == "Ion"
    assert getGen_carte(vanzare) == "literatura"
    assert getPret(vanzare) == 10
    assert getTip_reducere_client(vanzare) == "silver"