choice_loop_start = "Please make a selection\n"
choice_loop_end = "Go back to main"


def choice_loop(options, start=choice_loop_start,
                end=choice_loop_end):
    terminate = False
    while not terminate:

        print(start)

        options[end] = lambda: None

        user_choice = list_selection(list(options.keys()))

        if user_choice == end:
            terminate = True

        options[user_choice]()


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

