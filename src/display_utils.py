from os import system, name

choice_loop_start = "Please make a selection\n"
choice_loop_end = "Go back to main"


def choice_loop(options, start=choice_loop_start,
                end=choice_loop_end, prompt="", refresh_object=None):
    # refresh object will be displayed on a clear screen.
    # start text will then be displayed
    # list selection must point to callable object
    # end option automatically generated
    # loop continues as long as user does not call end option
    terminate = False
    while not terminate:
        clear_screen()
        if refresh_object:
            print(refresh_object)
        print(start)
        options['items'][end] = None
        user_choice = list_selection(options, prompt=prompt)

        if user_choice:
            user_choice()
        else:
            terminate = True


def list_selection(*option_blocks, multi=1, prompt="", col_width=30, blank=False):
    display = prompt
    if prompt:
        display += '\n\n'

    # check for titles, then add to display render
    render_titles = title_exists(*option_blocks)
    if render_titles:
        for block in option_blocks:
            display += "{0:<{width}}".format(block['title'], width=col_width)
        display += "\n\n"

    # prepend option number to every option
    # then combine each column into single string
    option_counter = 0
    columns = []
    for block in option_blocks:
        column = ""
        items = block['items'].keys()
        for item in items:
            option_counter += 1
            column += f"{option_counter}: {item}\n"
        columns.append(column)

    total_options = option_counter

    first_block_length = len(option_blocks[0]['items'].keys())

    # render based on amount of items and columns
    if len(option_blocks) > 1:
        # render columns side-by-side
        columns = render_columns(columns, col_width=col_width)
    elif first_block_length > 10:
        # split large column into multi then side-by-side render
        columns = split_column(columns[0])
        columns = render_columns(columns, col_width=col_width)
    else:
        columns = columns[0]

    display += columns

    # retrieve required number of selections
    chosen_indexes = None
    while not chosen_indexes:
        print(display)
        choice = input(">> ")
        if not choice and blank:
            return None

        chosen_indexes = convert_input_to_int(choice, 1, total_options, multi)

    # retrieve desired object(s)
    choices = []
    for index in chosen_indexes:
        choice = get_targeted_option(index - 1, *option_blocks)
        choices.append(choice)

    if len(choices) == 1:
        return choices[0]
    else:
        return tuple(choices)


def title_exists(*option_blocks):
    for block in option_blocks:
        if "title" not in block.keys():
            return False

    return True


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


def render_columns(columns, col_width=30):
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

            result += "{0:<{width}}".format(line_str, width=col_width)
        result += "\n"

    return result


def convert_input_to_int(user_input, min, max, multi=1):
    valid_message = "Please input {}."
    singular = "a valid number"
    plural = "valid numbers"
    quantity_message = "Please input the correct amount of numbers."
    if multi > 1:
        valid_message = valid_message.format(plural)
    else:
        valid_message = valid_message.format(singular)

    try:
        user_input = user_input.split()
        nums = []
        for i in range(0, multi):
            nums.append(int(user_input[i]))
    except ValueError:
        print(valid_message)
        return None
    except IndexError:
        print(quantity_message)
        return None

    for num in nums:
        if not min <= num <= max:
            print(valid_message)
            return None

    return nums


def user_confirmation(prompt):
    answer = None
    valid_answers = "yn"
    error_message = "Please type 'y' or 'n'"
    while not answer or answer not in valid_answers:

        answer = input(prompt).lower()
        if not answer or answer not in valid_answers:
            print(error_message)

    if answer == "y":
        return True
    else:
        return False


def get_targeted_option(index, *option_blocks):
    for block in option_blocks:
        items = list(block['items'].keys())
        if index < len(items):
            target_key = items[index]
            return block['items'][target_key]
        else:
            index -= len(items)


def create_option_block(title=""):
    options = {
        "items": {}
    }
    if title:
        options['title'] = title

    return (options, options['items'])


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
