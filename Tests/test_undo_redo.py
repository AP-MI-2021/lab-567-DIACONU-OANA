from Logic.crud import create
from UserInterface.console import handle_undo, handle_redo


def test_undo_redo():
    rezervari =[]
    undo_list=[]
    redo_list=[]
    rezervari = create(rezervari,1,'Pescaru','business',1000,'da',undo_list,redo_list)
    assert len(rezervari) == 1
    rezervari= create(rezervari,2,'Bratu','economy plus',485,'nu',undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari= create(rezervari,3,'Bratu','economy',100,'da',undo_list,redo_list)
    assert len(rezervari)== 3
    rezervari=handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari=handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 1
    rezervari=handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 0
    rezervari=handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 0
    rezervari = create(rezervari, 1, 'Pescaru', 'business', 1000, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'Bratu', 'economy plus', 485, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'Bratu', 'economy', 100, 'da', undo_list, redo_list)
    assert len(rezervari)== 3
    rezervari =handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 3
    rezervari = handle_undo(rezervari,undo_list,redo_list)
    rezervari = handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 1
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 3
    rezervari = handle_undo(rezervari,undo_list,redo_list)
    rezervari = handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 1
    rezervari = create(rezervari,3,'Costache','economy',100,'da',undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari = handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 1
    rezervari= handle_undo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 0
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 2
    rezervari = handle_redo(rezervari,undo_list,redo_list)
    assert len(rezervari)== 2





