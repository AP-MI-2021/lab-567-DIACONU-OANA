from Domain.rezervare import creeaza_rezervare
from Logic.pretul_maxim_pe_clasa import get_pretul_maxim_pe_clasa


def get_data():
    return [
        creeaza_rezervare(1,'Pescaru','business',1000,'da' ),
        creeaza_rezervare(2, 'Bratu','economy plus',485,'nu'),
        creeaza_rezervare(3,'Sorin','economy',100,'da'),
        creeaza_rezervare(4,'Crina','economy plus',467,'da'),
        creeaza_rezervare(5,'Bianca','business',1053,'nu'),
]


def test_get_pretul_maxim_pe_clasa():
    rezervari = get_data()
    maxim_clasa = get_pretul_maxim_pe_clasa(rezervari)
    assert maxim_clasa['economy'] == 100
    assert maxim_clasa['economy plus'] == 485
    assert maxim_clasa['business'] == 1053
