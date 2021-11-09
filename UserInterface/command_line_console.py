from Domain.rezervare import creeaza_rezervare
from Logic.crud import create, delete, update
from UserInterface.console import handle_show_all

def main_line(rezervari):
        while True:

                print('Daca solicitati detalii despre optiuni scrieti: help : ')
                optiunea=input('Optiunea ')
                if optiunea == 'help':
                    print('Pentru a adauga o noua rezervare scrieti add, urmat de datele rezervarii')
                    print('ex:add, id_rezervare, nume, clasa, pret, checkin;')
                    print('Pentru a modifica o rezervare scrieti update, urmat de id_rezervare si noile date')
                    print('ex:update, id_rezervare, nume_nou, clasa_noua, pret_nou, checkin_nou;')
                    print('Pentru a sterge o rezervare scrieti delete, urmat de id_rezervare')
                    print('ex:delete,id_rezervare;')
                    print('Pentru a afisa toate rezervarile scrieti showall')
                    print('ex:showall')
                    print('Pentru a iesi scrieti: stop')
                    print('Fiecare opriune trebuie separata prin ";" si fiecare componenta a unei optiuni trebuie separata prin "," ')
                else:
                    executa_optiuni = optiunea.split(";")
                    for i in range(len(executa_optiuni)):
                        optiune_separata = executa_optiuni[i].split(",")
                        if optiune_separata[0] == 'add':
                            if len(optiune_separata) != 6:
                                raise ValueError(" Trebuie sa introduceti exact 5 date! ")
                            id_rezervare= int(optiune_separata[1])
                            nume= optiune_separata[2]
                            clasa= optiune_separata[3]
                            pret= float(optiune_separata[4])
                            checkin= optiune_separata[5]
                            print('rezervarea a fost adaugata cu succes!')
                            rezervari =create(rezervari,id_rezervare, nume, clasa, pret, checkin)
                        elif optiune_separata[0] =='delete':
                            id_rezervare = int(optiune_separata[1])
                            print("Rezervarea a fost stearsa cu succes!")
                            rezervari= delete(rezervari,id_rezervare)
                        elif optiune_separata[0] =='update':
                            if len(optiune_separata) != 6:
                                raise ValueError("Trebuie sa introduceti exact 5 date!")
                            id_rezervare= int(optiune_separata[1])
                            nume= optiune_separata[2]
                            clasa= optiune_separata[3]
                            pret= float(optiune_separata[4])
                            checkin= optiune_separata[5]
                            print('Rezervarea a fost modificata cu succes!')
                            rezervari= update(rezervari,creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin))
                        elif optiune_separata[0] =='showall':
                            handle_show_all(rezervari)
                        elif optiune_separata[0] =='stop':
                            return rezervari
                        else:
                            print('Optiune invalida!')




















