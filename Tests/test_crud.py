from Domain.rezervare import creeaza_rezervare, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_rezervare(1,'Diaconu','business',1000,'da' ),
        creeaza_rezervare(2, 'Dobre','economy plus',485,'nu'),
        creeaza_rezervare(3,'Costache','economy',100,'da'),
        creeaza_rezervare(4,'Popa','economy plus',467,'da'),
        creeaza_rezervare(5,'Pirvan','business',1053,'nu'),
    ]

def test_create():
    rezervari = get_data()
    params = (6, 'Gherman','economy',67,'nu')
    r_new = creeaza_rezervare(*params)
    new_rezervari= create(rezervari, *params)
    assert len(new_rezervari) == len(rezervari) + 1
    assert r_new in new_rezervari

    #testam daca se lanseaza exceptie pentru id duplicat

    params2 =(6, 'Stancu', 'economy plus',654,'nu')
    try:
        some_r =create(new_rezervari, *params2)
        assert False
    except ValueError:
        assert True

def test_read():
    rezervari = get_data()
    some_r = rezervari[2]
    assert read(rezervari, get_id(some_r)) == some_r


def test_update():
    rezervari = get_data()
    r_updated = creeaza_rezervare(1, 'new name','economy',200,'da')
    updated = update(rezervari, r_updated)
    assert r_updated in updated
    assert r_updated not in rezervari
    assert len(updated) == len(rezervari)


def test_delete():
    rezervari = get_data()
    to_delete = 2
    r_deleted = read(rezervari, to_delete)
    deleted = delete(rezervari, to_delete)
    assert r_deleted not in deleted
    assert r_deleted in rezervari
    assert len(deleted) == len(rezervari) - 1
