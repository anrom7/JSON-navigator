import json


def get_json_object(file_path: str) -> dict:
    """
    Serialize json object from a file
    """
    with open(file_path) as file:
        file = json.load(file)
    return file


def navigate(obj, next_key):
    """
    Navigate json object
    """
    confirm_message = "(yes - any key / no - empty space)"
    if next_key:
        obj = obj[next_key]
    if isinstance(obj, dict):
        keys = list(obj)
        print(', '.join(keys))
        user_key = input("This is a dict. Enter a key from the above list:\n")
        if user_key in obj:
            return navigate(obj, user_key)
        print("There's no such a key")
        return navigate(obj, next_key)
    elif isinstance(obj, list):
        entire_lst = input("This is a list. Do you want to display the entire list?"
                           f" {confirm_message}\n")
        if entire_lst:
            print(obj)
        while True:
            obj_idx = input(f"Enter an index in range from 0 to {len(obj) - 1}\n")
            if obj_idx.isdigit() and 0 <= int(obj_idx) <= len(obj) - 1:
                break
        return navigate(obj, int(obj_idx))
    else:
        display_value = input(f"This is a {type(obj)}. Do you want to display its value?"
                              f" {confirm_message}\n")
        if display_value:
            return obj
        return "Nothing to show..."
