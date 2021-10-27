from Domain.rezervare import get_str
from Logic.crud import create


def show_menu():
    print('1.CRUD')
    print('2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
    print('x.Exit')


def handle_add(rezervari):
    id_rezervare= int(input('Dati id-ul rezervarii: '))
    nume = input('Dati numele rezervarii: ')
    clasa = input('Alegeti clasa rezervarii: ')
    pret = input('Dati pretul rezervarii: ')
    checkin = input('Confirmati checkin-ul rezervarii: ')
    return create(rezervari,id_rezervare,nume,clasa,pret,checkin)


def handle_crud(rezervari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')

        optiune= input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida!')
    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def run_ui(rezervari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')

    return rezervari