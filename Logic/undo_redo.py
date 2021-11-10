def do_undo(undo_list: list,redo_list: list,current_list: list):
    """
    :param undo_list:anuleaza modificarile listei
    :param redo_list:anuleaza undo
    :param current_list:
    :return:
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None

def do_redo(undo_list: list,redo_list: list):
    """
    :param undo_list: anuleaza modificarile listei
    :param redo_list: anuleaza undo
    :return:
    """
    if redo_list:
        top_redo=redo_list.pop()
        undo_list.append(top_redo)
        return top_redo
    return None