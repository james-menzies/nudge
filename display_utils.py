def list_selection(items):
    chosen_index = None

    while not chosen_index:
        for index, item in enumerate(items):
            print(f"{index + 1}: {item}")

        print()
        choice = input(">> ")
        chosen_index = convert_input_to_int(choice, 1, len(items))

    return items[chosen_index - 1]


def convert_input_to_int(user_input, min, max):
    err_message = "Please input a valid number."
    try:
        user_input = int(user_input)
    except ValueError:
        print(err_message)
        return None

    if min <= user_input <= max:
        return user_input
    else:
        print(err_message)
        return None
