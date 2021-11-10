from Domain.vanzare import toString
from Logic.CRUD import adaugareVanzare, stergereVanzare


def showAll(l):
    for vanzare in l:
        print(toString(vanzare))

def main_line(l):
    print("Scrieti ajutor pentru a vedea optiunile disponibile sau dati comanda: ")
    while True:
        giveString = input()
        if giveString == "ajutor":
            print("adugare , id, titlu_carte, gen_carte, pret, tip_reducere_client")
            print("stergere, id")
            print("showAll")
            print("Iesire")
        else:
            optiuni = giveString.split(";")
            if optiuni[0] == "Iesire":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if(opt[0] == "adaugare"):
                        try:
                            lista = adaugareVanzare(opt[1], opt[2], opt[3], opt[4], opt[5], lista)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showAll":
                        showAll(lista)
                    elif opt[0] == "stergere":
                        lista = stergereVanzare(opt[1], lista)
                    else:
                        print("Optiune gresita! Scrieti -ajutor- pentru a vedea optiunile")