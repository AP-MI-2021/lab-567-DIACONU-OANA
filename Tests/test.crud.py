from Domain.rezervare import creeaza_rezervare
from Logic.crud import create


def get_data():
    return [
        creeaza_rezervare(1,'Diaconu','business',1000,'da' )
        creeaza_rezervare(2, 'Dobre','economy plus',485,'nu')
        creeaza_rezervare(3, 'Costache','economy',100,'da')
        creeaza_rezervare(4, 'Popa','economy plus',467,'da')
        creeaza_rezervare(5, 'Pirvan','business',1053,'nu' )
    ]

def test_create():
    rezervari = get_data()
    params = (6, 'Gherman','economy',67,'nu')
    r_new = creeaza_rezervare(*params)
    new_rezervari= create(rezervari, *params)
    assert len(new_rezervari) == len(rezervari) + 1
    assert r_new in new_rezervari

