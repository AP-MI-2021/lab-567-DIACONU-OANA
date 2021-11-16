from Domain.rezervare import creeaza_rezervare, get_id, get_pret, get_clasa
from Logic.clasa_superioara import trecere_la_clasa_superioara
from Logic.ieftinire_pret import ieftinire_pret_dupa_checkin
from UserInterface.console import handle_undo, handle_redo


def get_data():
    return [
        creeaza_rezervare(1,'Pescaru','business',1000,'da' ),
        creeaza_rezervare(2,'Bratu','economy plus',485,'nu'),
        creeaza_rezervare(3,'Bratu','economy',100,'da'),
        creeaza_rezervare(4,'Bratu','economy plus',467,'da'),
        creeaza_rezervare(5,'Bianca','business',1053,'nu'),
]

def test_ieftinire_pret_dupa_checkin_undo_redo():
    rezervari = get_data()
    undo_list=[]
    redo_list=[]
    r_new = ieftinire_pret_dupa_checkin(rezervari, 'da', 10,undo_list,redo_list)
    for rezervare in r_new:
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
    r_new = handle_undo(r_new,undo_list,redo_list)
    for rezervare in r_new:
        if get_id(rezervare) == 1:
            assert get_pret(rezervare) == 1000
        elif get_id(rezervare) == 2:
            assert get_pret(rezervare) == 485
        elif get_id(rezervare) == 3:
            assert get_pret(rezervare) == 100
        elif get_id(rezervare) == 4:
            assert get_pret(rezervare) == 467
        elif get_id(rezervare) == 5:
            assert get_pret(rezervare) == 1053
    r_new= handle_redo(r_new,undo_list,redo_list)
    for rezervare in r_new:
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


def test_trecere_la_clasa_superioara_undo_redo():
    rezervari = get_data()
    undo_list=[]
    redo_list=[]
    r_new = trecere_la_clasa_superioara(rezervari,'Bratu',undo_list,redo_list)
    for rezervare in r_new:
        if get_id(rezervare) == 1:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 2:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 3:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 4:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 5:
            assert get_clasa(rezervare) == 'business'
    r_new =handle_undo(r_new,undo_list,redo_list)
    for rezervare in r_new:
        if get_id(rezervare) == 1:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 2:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 3:
            assert get_clasa(rezervare) == 'economy'
        elif get_id(rezervare) == 4:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 5:
            assert get_clasa(rezervare) == 'business'
    r_new=handle_redo(r_new,undo_list,redo_list)
    for rezervare in r_new:
        if get_id(rezervare) == 1:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 2:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 3:
            assert get_clasa(rezervare) == 'economy plus'
        elif get_id(rezervare) == 4:
            assert get_clasa(rezervare) == 'business'
        elif get_id(rezervare) == 5:
            assert get_clasa(rezervare) == 'business'
