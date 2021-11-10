from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_checkin, get_pret


def create(lst_rezervari, id_rezervare: int, nume, clasa, pret: float, checkin, undo_list: list, redo_list: list):
    '''
    Creeaza rezervarile companiei aeriene.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii, trebuie sa fie unic
    :param nume: numele rezervarii, nenul
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkin: checkinul rezervarii
    :param undo_list: anuleaza  modificarile listei
    param redo_list: anuleaza undo
    :return: o noua lista formata din lst_rezervari si noua rezervare adaugata
    '''

    if read(lst_rezervari,id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')

    if len(nume) == 0:
        raise ValueError(f'Numele rezervarii nu poate fi lasat necompletat')

    if clasa != 'economy' and clasa !='economy plus' and clasa!='business':
        raise ValueError(f'Clasa trebuie sa corespunda cu una din optiunile:economy,economy plus,business')

    if checkin!='da' and checkin!='nu':
        raise ValueError(f'Valorile pe care le poate lua checkin-ul sunt :da sau nu')

    if float(pret) <= 0:
        raise ValueError(f'Pretul trebuie sa fie >0')


    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return lst_rezervari + [rezervare]


def read(lst_rezervari, id_rezervare:int = None):
    '''
    Citeste o rezervare din baza de date.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :return: -rezervarea cu id-ul id_rezervare daca exista
             -toata lista cu rezervari daca id_rezervare= None
             -None, daca nu exista rezervare cu id_rezervare
    '''


    if not id_rezervare:
        return lst_rezervari

    rezervare_cu_id= None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return None


def update(lst_rezervari, new_rezervare, undo_list: list, redo_list: list):
    '''
    Actualizeaza o rezervare.
    :param lst_rezervari: lista de rezervari
    :param new_rezervare: rezervarea care se va actualiza - id-ul trebuie sa fie unul existent
    :param undo_list: anuleaza  modificarile listei
    :param redo_list: anuleaza undo
    :return: o lista de rezevari actualizata
    '''

    if read(lst_rezervari,get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista  o rezervare cu id-ul {get_id(new_rezervare)} pe care sa o actualizam')

    if len(get_nume(new_rezervare)) == 0:
        raise ValueError(f'Numele rezervarii nu poate fi lasat necompletat')

    if get_clasa(new_rezervare) != 'economy' and get_clasa(new_rezervare) !='economy plus' and get_clasa(new_rezervare)!='business':
        raise ValueError(f'Clasa trebuie sa corespunda cu una din optiunile:economy,economy plus,business')

    if get_checkin(new_rezervare)!='da' and get_checkin(new_rezervare)!='nu':
        raise ValueError(f'Valorile pe care le poate lua checkin-ul sunt :da sau nu')

    if float(get_pret(new_rezervare)) <= 0:
        raise ValueError(f'Pretul trebuie sa fie >0')

    new_rezervari= []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return new_rezervari


def delete(lst_rezervari, id_rezervare:int, undo_list: list, redo_list: list):
    '''
    Sterge o rezervare din baza de date.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :param undo_list: anuleaza modificarile listei
    :param redo_list: anuleaza redo
    :return: o lista de rezervari fara rezervarea cu id-ul id_rezervare
    '''

    if read(lst_rezervari,id_rezervare) is None:
        raise ValueError(f'Nu exista  o rezervare cu id-ul {id_rezervare} pe care sa o stergem')


    new_rezervari= []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return new_rezervari



