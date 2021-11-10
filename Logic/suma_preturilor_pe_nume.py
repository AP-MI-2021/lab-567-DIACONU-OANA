from Domain.rezervare import get_pret, get_nume


def suma_preturilor_pe_nume(lst_rezervari):
    '''
    Afișarea sumelor prețurilor pentru fiecare nume.
    :param lst_rezervari: lista de rezervari
    :return: un dictionar in care  cheiea este numele si valoarea este suma preturilor pe fiecare nume.
    '''

    result={}
    for rezervare in lst_rezervari:
        pret=get_pret(rezervare)
        nume=get_nume(rezervare)
        if nume  not in result:
            result[nume]= pret
        else:
            result[nume] += pret
    return result