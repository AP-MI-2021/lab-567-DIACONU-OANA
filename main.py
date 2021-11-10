from Logic.crud import create
from Tests.ordonare import test_ordonarea_rezervarilor_dupa_pret
from Tests.pretul_maxim import test_get_pretul_maxim_pe_clasa
from Tests.suma_preturilor import test_suma_preturilor_pe_nume
from Tests.test_crud import test_create, test_read, test_update, test_delete
from Tests.test_ieftinire_pret import test_ieftinire_pret_dupa_checkin
from Tests.test_trecere import test_trecere_la_clasa_superioara
from UserInterface.command_line_console import main_line
from UserInterface.console import run_ui


def main():
    rezervari = []
    undo_list = []
    redo_list= []
    rezervari= create(rezervari, 8,'Gherman','business',4000.0,'da',undo_list,redo_list)
    rezervari = create(rezervari, 9, 'Popescu', 'economy', 456.0, 'da',undo_list,redo_list)
    rezervari = create(rezervari, 10, 'Simionescu', 'business', 8349.0, 'nu',undo_list,redo_list)
    rezervari = create(rezervari, 11, 'Cretu', 'economy plus', 123.0, 'da',undo_list,redo_list)
    rezervari = create(rezervari, 12, 'Burtescu', 'economy', 839.0, 'nu',undo_list,redo_list)
    rezervari = create(rezervari, 13, 'Cretu', 'economy', 545.89, 'nu',undo_list,redo_list)
    rezervari = create(rezervari, 14, 'Burtescu', 'economy plus', 1000.0, 'da',undo_list,redo_list)
    rezervari = create(rezervari, 15, 'Simionescu', 'economy', 23, 'nu',undo_list,redo_list)
    meniu= str(input('Alegeti meniul pe care doriti sa-l utilizati: clasic sau linie: '))
    if meniu == 'clasic':
        run_ui(rezervari,undo_list,redo_list)
    elif meniu == 'linie':
        main_line(rezervari)




if __name__ == '__main__':
  test_create()
  test_read()
  test_update()
  test_delete()
  test_ieftinire_pret_dupa_checkin()
  test_trecere_la_clasa_superioara()
  test_get_pretul_maxim_pe_clasa()
  test_suma_preturilor_pe_nume()
  test_ordonarea_rezervarilor_dupa_pret()
  main()