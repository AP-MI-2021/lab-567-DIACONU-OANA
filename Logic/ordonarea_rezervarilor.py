from Domain.rezervare import get_pret


def dupa_pret(rezervare):
    return get_pret(rezervare)


def ordonarea_rezervarilor_dupa_pret(lst_rezervari):
    return sorted(lst_rezervari, key=dupa_pret,reverse=True)