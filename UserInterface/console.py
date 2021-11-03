from Domain.rezervare import get_str, get_nume, get_clasa, get_pret, get_checkin, creeaza_rezervare
from Logic.clasa_superioara import trecere_la_clasa_superioara
from Logic.crud import create, read, update, delete
from Logic.ieftinire_pret import ieftinire_pret_dupa_checkin


def show_menu():
    print('1.CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
    print('3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit')
    print('x.Exit')


def handle_add(rezervari):
    try:

        id_rezervare= int(input('Dati id-ul rezervarii: '))
        nume = input('Dati numele rezervarii: ')
        clasa = input('Alegeti clasa rezervarii: ')
        pret = input('Dati pretul rezervarii: ')
        checkin = input('Confirmati checkin-ul rezervarii: ')
        return create(rezervari,id_rezervare,nume,clasa,pret,checkin)

    except ValueError as ve:
        print('Eroare:',ve)

    return rezervari

def handle_show_detalis(rezervari):
    id_rezervare= int(input('Dati id-ul rezervarii pentru care doriti detalii: '))
    rezervare= read(rezervari,id_rezervare)
    print(f'Nume: {get_nume(rezervare)} ')
    print(f'clasa: {get_clasa(rezervare)} ')
    print(f'pret: {get_pret(rezervare)} ')
    print(f'checkin: {get_checkin(rezervare)} ')


def handle_update(rezervari):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se actualizeaza: '))
        nume = input('Dati noul nume al rezervarii: ')
        clasa = input('Alegeti noua clasa a rezervarii: ')
        pret = input('Dati noul pret al  rezervarii: ')
        checkin = input('Confirmati noul checkin al rezervarii: ')
        return update(rezervari,creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin))
    except ValueError as ve:
        print('Eroare: ',ve)

    return rezervari

def handle_delete(rezervari):
    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se sterge: '))
        rezervari = delete(rezervari,id_rezervare)
        print('Stergerea a fost efectuata cu succes.')
        return rezervari
    except ValueError as ve:
        print('Eroare: ',ve)

    return rezervari

def handle_crud(rezervari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii rezervare')
        print('b. Revenire')

        optiune= input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari)
        elif optiune == '2':
            rezervari = handle_update(rezervari)
        elif optiune == '3':
            rezervari = handle_delete(rezervari)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'd':
            handle_show_detalis(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida!')
    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_ieftinire_pret(rezervari):
    try:
        checkin = 'da'
        procentaj = float(input('Dati procentajul cu care se va reduce pretul (intre 0 si 100): '))
        rezervari= ieftinire_pret_dupa_checkin(rezervari,checkin,procentaj)
        print('Preturile au fost reduse cu succes')

    except ValueError as ve:
        print('Eroare: ',ve)

    return rezervari



def handle_trecerea_la_clasa_superioara(rezervari):
    try:
        nume= str(input('Dati numele care va determina trecerea la o clasa superioara: '))
        rezervari= trecere_la_clasa_superioara(rezervari,nume)
        print('Trecerea a fost realizata cu succes')

    except ValueError as ve:
        print('Eroare: ',ve)

    return rezervari


def run_ui(rezervari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == '2':
            rezervari = handle_trecerea_la_clasa_superioara(rezervari)
        elif optiune == '3':
            rezervari= handle_ieftinire_pret(rezervari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

    return rezervari