from Domain.rezervare import get_id, get_pret, creeaza_rezervare
from Logic.ieftinire_pret import ieftinire_pret_dupa_checkin


def get_data():
    return [
        creeaza_rezervare(1,'Pescaru','business',1000,'da' ),
        creeaza_rezervare(2, 'Bratu','economy plus',485,'nu'),
        creeaza_rezervare(3,'Sorin','economy',100,'da'),
        creeaza_rezervare(4,'Crina','economy plus',467,'da'),
        creeaza_rezervare(5,'Bianca','business',1053,'nu'),
]

def test_ieftinire_pret_dupa_checkin():
    rezervari = get_data()
    rezervari = ieftinire_pret_dupa_checkin(rezervari,'da', 10)
    for rezervare in rezervari:
        if get_id(rezervare) == 1:
            assert get_pret(rezervare) == 900.0
        elif get_id(rezervare) == 2:
            assert get_pret(rezervare) == 485
        elif get_id(rezervare) == 3:
            assert get_pret(rezervare) == 90.0
        elif get_id(rezervare) == 4:
            assert get_pret(rezervare) == 420.3
        elif get_id(rezervare) == 5:
            assert get_pret(rezervare) == 1053


