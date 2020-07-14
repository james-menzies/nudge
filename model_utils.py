player_init_error = "Wrong data type submitted in model construction"


def check_type(obj, obj_type):
    if isinstance(obj, obj_type):
        return obj

    elif isinstance(obj, list):
        new_list = []
        for item in obj:
            if isinstance(item, obj_type):
                new_list.append(item)
    else:
        raise ValueError(player_init_error)
