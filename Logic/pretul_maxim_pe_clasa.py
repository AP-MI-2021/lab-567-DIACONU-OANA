from Domain.rezervare import get_pret, get_clasa


def get_pretul_maxim_pe_clasa(lst_rezervari):
    '''
    Determinarea prețului maxim pentru fiecare clasă
    :param lst_rezervari: lista de rezervari
    :return:un dictionar in care cheia este clasa si valoarea este pretul maxim din acea clasa
    '''

    result={}
    for rezervare in lst_rezervari:
        pret=get_pret(rezervare)
        clasa=get_clasa(rezervare)
        if clasa not in result:
            result[clasa]= pret
        else:
            if pret> result[clasa]:
                result[clasa]=pret
    return result


