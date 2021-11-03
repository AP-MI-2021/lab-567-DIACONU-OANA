from Domain.rezervare import get_id, get_clasa, creeaza_rezervare
from Logic.clasa_superioara import trecere_la_clasa_superioara


def get_data():
    return [
        creeaza_rezervare(1,'Popovici','economy',546,'nu' ),
        creeaza_rezervare(2, 'Marlena','economy plus',344,'nu'),
        creeaza_rezervare(3,'Marlena','economy',45,'da'),
        creeaza_rezervare(4,'Anton','economy plus',234,'da'),
        creeaza_rezervare(5,'Marlena','business',789,'da'),
]

def test_trecere_la_clasa_superioara():
    rezervari = get_data()
    rezervari = trecere_la_clasa_superioara(rezervari,'Marlena')
    for rezervare in rezervari:
        if get_id(rezervare) == 1:
            assert get_clasa(rezervare) == 'economy'
        elif get_id(rezervare) == 2:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 3:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 4:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 5:
            assert get_clasa(rezervare) == 'business'