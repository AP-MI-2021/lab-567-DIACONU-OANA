from Domain.rezervare import get_pret, creeaza_rezervare
from Logic.ordonarea_rezervarilor import ordonarea_rezervarilor_dupa_pret


def get_data():
    return [
        creeaza_rezervare(1,'Pescaru','business',1000,'da' ),
        creeaza_rezervare(2, 'Bratu','economy plus',485,'nu'),
        creeaza_rezervare(3,'Sorin','economy',100,'da'),
        creeaza_rezervare(4,'Crina','economy plus',467,'da'),
        creeaza_rezervare(5,'Bianca','business',1053,'nu'),
]


def test_ordonarea_rezervarilor_dupa_pret():
    rezervari = get_data()
    ord_rezervari= ordonarea_rezervarilor_dupa_pret(rezervari)
    assert get_pret(ord_rezervari[0]) == 1053
    assert get_pret(ord_rezervari[1]) == 1000
    assert get_pret(ord_rezervari[2]) == 485
    assert get_pret(ord_rezervari[3]) == 467
    assert get_pret(ord_rezervari[4]) == 100
