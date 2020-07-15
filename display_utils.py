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
    display = []

    for index, item in enumerate(items):
        display.append(f"{index + 1}: {item}")




    if len(items) > 20:
        num_columns = 3
    elif len(items) > 10:
        num_columns = 2
    else:
        num_columns = 1


    while not chosen_index:
        for line in display:
            print(line)

        print()
        choice = input(">> ")
        chosen_index = convert_input_to_int(choice, 1, len(items))

    return items[chosen_index - 1]


def render_columns(columns):
    max_rows = 0

    result = ""

    for index, column in enumerate(columns):
        column = str(column)
        column = column.split(sep="\n")
        columns[index] = column
        if len(column) > max_rows:
            max_rows = len(column)

    for i in range(0, max_rows):
        for column in columns:
            if i >= len(column):
                name_str = ""
            else:
                name_str = column[i]

            result += "{0:30}".format(name_str)
        result += "\n"

    return result


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
