def creeaza_rezervare(id_rezervare: int, nume, clasa, pret: float, checkin):
    '''
    Creeaza o rezervare.
    :param id_rezervare: id-ul rezervarii, trebuie sa fie unic.
    :param nume: numele pasagerului, nenul 
    :param clasa: clasa rezervata, (economy,economy plus,business)
    :param pret: pretul rezervarii
    :param checkin: verificarea checkin-ului
    :return: o rezervare 
    '''

    return[id_rezervare, nume, clasa, pret,checkin]


def get_id(rezervare):
    '''
    Getter pentru id-ul rezervarii.
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    '''
    return rezervare[0]


def get_nume(rezervare):
    '''
    Getter pentru numele pe care este facuta rezervarea.
    :param rezervare: rezervarea
    :return:numele rezervarii date ca parametru
    '''
    return rezervare[1]


def get_clasa(rezervare):
    '''
    Getter pentru clasa rezervarii .
    :param rezervare: rezervarea
    :return:clasa rezervarii date ca parametru
    '''
    return rezervare[2]


def get_pret(rezervare):
    '''
    Getter pentru pretul rezervarii .
    :param rezervare: rezervarea
    :return:pretul rezervarii date ca parametru
    '''
    return rezervare[3]


def get_checkin(rezervare):
    '''
    Getter pentru checkin-ul rezervarii .
    :param rezervare: rezervarea
    :return:checkin-ul rezervarii date ca parametru
    '''
    return rezervare[4]


def get_str(rezervare):
    return f'Rezervarea cu id-ul {get_id(rezervare)}, pe numele {get_nume(rezervare)}, la clasa {get_clasa(rezervare)},cu pretul {get_pret(rezervare)},cu checkin {get_checkin(rezervare)}'

