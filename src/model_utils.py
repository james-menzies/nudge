player_init_error = "Attempted to assign the wrong data type to a model object"


def check_type(obj, obj_type, throw=True):
    if isinstance(obj, obj_type):
        return obj

    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            if isinstance(item, obj_type):
                new_list.append(item)
        return new_list
    elif throw:
        raise ValueError(player_init_error)
    else:
        return None
