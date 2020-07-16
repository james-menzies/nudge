from display_utils import *

def pop_items():

    items = {}

    for i in range(1, 14):
        items[f"Option #{i}"] = i

    return items


block1 = {
    "title": "Group 1",
}

block2 = {
    "title": "Group 2",
}


block1['items'] = pop_items()
block2['items'] = pop_items()

results = list_selection(block1, block2, multi=2)

for result in results:
    print(f"You selected {result}")

