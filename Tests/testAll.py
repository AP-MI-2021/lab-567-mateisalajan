from Tests.testCrud import testAdaugaVanzare, testStergePrajitura, testModificaVanzare
from Tests.testDomeniu import testVanzare
from Tests.testFunctionaliati import testDiscount, testModificare_gen, testPretMinimGen


def runAllTests():
    testVanzare()
    testAdaugaVanzare()
    testStergePrajitura()
    testModificaVanzare()

    testDiscount()
    testModificare_gen()
    testPretMinimGen()