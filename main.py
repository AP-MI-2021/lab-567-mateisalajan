from Logic.CRUD import adaugareVanzare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugareVanzare("1", "Ion", "literatura", 10, "silver", lista)
    lista = adaugareVanzare("2", "Poezii", "literatura", 27, "none", lista)
    runMenu(lista)

if __name__ == '__main__':
    main()