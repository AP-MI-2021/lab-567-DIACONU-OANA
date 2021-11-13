from Domain.rezervare import get_checkin, creeaza_rezervare, get_id, get_nume, get_clasa, get_pret


def ieftinire_pret_dupa_checkin(lst_rezervari, continut_checkin, procentaj,undo_list,redo_list):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit
    :param lst_rezervari: lista de rezervari
    :param continut_checkin: checkin-ul rezervarii (da/nu)
    :param procentaj: Procentul cu care se reduce pretul,(intre 0 si 100)
    :param undo_list: o lista care memoreaza lista de rezervari inainte de ieftinire
    :param redo_list:o lista care memoreaza lista de rezervari dupa ieftinire
    :return: o noua lista cu pretul redus
    '''

    if not(0<= procentaj <= 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100 inclusiv.')

    result = []
    for rezervare in lst_rezervari:
        if continut_checkin in get_checkin(rezervare):
            pret_nou =  get_pret(rezervare) - (procentaj / 100) * get_pret(rezervare)
            result.append(creeaza_rezervare(get_id(rezervare),get_nume(rezervare),get_clasa(rezervare),pret_nou,get_checkin(rezervare)))
        else:
            result.append(rezervare)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result
