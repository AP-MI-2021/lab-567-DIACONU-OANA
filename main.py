from Logic.crud import create
from Tests.test_crud import test_create, test_read, test_update, test_delete
from Tests.test_ieftinire_pret import test_ieftinire_pret_dupa_checkin
from Tests.test_trecere import test_trecere_la_clasa_superioara
from UserInterface.console import run_ui


def main():
    rezervari = []
    rezervari= create(rezervari, 8,'Gherman','bussines',4000,'da')
    rezervari = create(rezervari, 9, 'Popescu', 'economy', 456, 'da')
    rezervari = create(rezervari, 10, 'Simionescu', 'bussines', 8349, 'nu')
    rezervari = create(rezervari, 11, 'Cretu', 'economy plus', 123, 'da')
    rezervari = create(rezervari, 12, 'Burtescu', 'economy', 839, 'nu')
    rezervari = run_ui(rezervari)


if __name__ == '__main__':
  test_create()
  test_read()
  test_update()
  test_delete()
  test_ieftinire_pret_dupa_checkin()
  test_trecere_la_clasa_superioara()
  main()