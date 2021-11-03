from Domain.rezervare import creeaza_rezervare, get_id


def create(lst_rezervari, id_rezervare: int, nume, clasa, pret, checkin):
    '''
    Creeaza rezervarile companiei aeriene.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii, trebuie sa fie unic
    :param nume: numele rezervarii, nenul
    :param clasa: clasa rezervarii
    :param pret: pretul rezervarii
    :param checkin: checkinul rezervarii
    :return: o noua lista formata din lst_rezervari si noua rezervare adaugata
    '''

    if read(lst_rezervari,id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')

    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
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


def update(lst_rezervari, new_rezervare):
    '''
    Actualizeaza o rezervare.
    :param lst_rezervari: lista de rezervari
    :param new_rezervare: rezervarea care se va actualiza - id-ul trebuie sa fie unul existent
    :return: o lista de rezevari actualizata
    '''

    if read(lst_rezervari,get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista  o rezervare cu id-ul {get_id(new_rezervare)} pe care sa o actualizam')

    new_rezervari= []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    return new_rezervari


def delete(lst_rezervari, id_rezervare:int):
    '''
    Sterge o rezervare din baza de date.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :return: o lista de rezervari fara rezervarea cu id-ul id_rezervare
    '''

    if read(lst_rezervari,id_rezervare) is None:
        raise ValueError(f'Nu exista  o rezervare cu id-ul {id_rezervare} pe care sa o stergem')

    new_rezervari= []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)
    return new_rezervari



