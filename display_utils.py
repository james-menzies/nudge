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

def title_exists(*option_blocks):

    for block in option_blocks:
        if "title" not in block.keys():
            return False

    return True

def list_selection(*option_blocks):

    display = ""
    # check for titles
    render_titles = title_exists(*option_blocks)
    if render_titles:
        for block in option_blocks:
            display += f"{block['title']:30}"
        display += "\n\n"

    option_counter = 1
    columns = []
    for block in option_blocks:
        column = ""
        items = block['items'].keys()
        for item in items:
            column += f"{option_counter}: {item}\n"
            option_counter += 1
        columns.append(column)

    total_options = option_counter

    first_block_length = len(option_blocks[0]['items'].keys())

    if len(option_blocks) > 1:
        columns = render_columns(columns)
    elif first_block_length > 10:
        columns = split_column(columns[0])
        columns = render_columns(columns)
    else:
        columns = columns[0]

    display += columns

    chosen_index = None
    while not chosen_index:
        print(display)
        print()
        choice = input(">> ")
        chosen_index = convert_input_to_int(choice, 1, total_options) - 1

    target_index = chosen_index
    for block in option_blocks:
        items = list(block['items'].keys())
        if target_index < len(items):
            target_key = items[target_index]
            return block['items'][target_key]
        else:
            target_index -= len(items)


def split_column(column):
    items = column.splitlines()
    length = len(items)
    columns = []
    if length > 20:
        num_columns = 3
    else:
        num_columns = 2

    base_amount = length // num_columns
    overlap = length % num_columns
    col_numbers = []
    for i in range(0, num_columns):
        if overlap > i:
            col_numbers.append(base_amount + 1)
        else:
            col_numbers.append(base_amount)

    iterator = iter(items)

    for num in col_numbers:
        new_column = ""
        for i in range(0, num):
            new_column += next(iterator) + "\n"
        columns.append(new_column)

    return columns


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
                line_str = ""
            else:
                line_str = column[i]

            result += "{0:30}".format(line_str)
        result += "\n"

    return result


def convert_input_to_int(user_input, min, max, multi=False):
    err_message = "Please input a valid number."
    try:
        user_input = user_input.split()
        num
    except ValueError:
        print(err_message)
        return None

    if min <= user_input <= max:
        return user_input
    else:
        print(err_message)
        return None
