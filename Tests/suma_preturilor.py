from Domain.rezervare import creeaza_rezervare
from Logic.suma_preturilor_pe_nume import suma_preturilor_pe_nume


def get_data():
    return [
        creeaza_rezervare(1,'Pescaru','business',1000,'da' ),
        creeaza_rezervare(2, 'Sorin','economy plus',485,'nu'),
        creeaza_rezervare(3,'Sorin','economy',100,'da'),
        creeaza_rezervare(4,'Pescaru','economy plus',467,'da'),
        creeaza_rezervare(5,'Bianca','business',1053,'nu'),
]


def test_suma_preturilor_pe_nume():
    rezervari = get_data()
    suma_preturilor = suma_preturilor_pe_nume(rezervari)
    assert suma_preturilor['Pescaru'] == 1467
    assert suma_preturilor['Sorin'] == 585
    assert suma_preturilor['Bianca'] == 1053