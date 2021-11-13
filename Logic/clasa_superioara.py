from Domain.rezervare import get_nume, creeaza_rezervare, get_id, get_pret, get_checkin, get_clasa


def trecere_la_clasa_superioara(lst_rezervari, continut_nume,undo_list,redo_list):
    """
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară
    :param lst_rezervari: lista de rezervari
    :param continut_nume: numele rezervarii
    :param clasa: clasa rezervarii
    :param undo_list:o lista care memoreaza lista de rezervari inainte de trecerea la o clasa superioara
    param redo_list:o lista care memoreaza lista de rezervari dupa trecerea la o clasa superioara
    :return: o noua lista cu clase modificate
    """

    if continut_nume == '':
        raise ValueError('Textul cautat nu poate fi gol.')

    result=[]
    for rezervare in lst_rezervari:
        if continut_nume in get_nume(rezervare):
            if get_clasa(rezervare)== 'economy':
                result.append(creeaza_rezervare(get_id(rezervare),get_nume(rezervare),'economy plus',get_pret(rezervare),get_checkin(rezervare)))
            elif get_clasa(rezervare)== 'economy plus':
                result.append(creeaza_rezervare(get_id(rezervare), get_nume(rezervare),'business',get_pret(rezervare),get_checkin(rezervare)))
        else:
             result.append(rezervare)
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result

