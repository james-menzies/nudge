from display_utils import *

options = []

option, items = create_option_block()

items["banana"] = 23.4
items["apple"] = 12.3
items["orange"] = 6.54

options.append(option)

option, items = create_option_block()

items["egg"] = 0.43
items["milk"] = 2.43
items["sponge"] = 7.56

options.append(option)


num = list_selection(*options)

print(num)