import json
main_data = None
def _remove_from_main_data(key, value):
    d = get_main_data()

    d[key].remove(value)

    _save_main_data(d)

def _save_main_data(new_data):
    with open("data.json", 'w') as f:
        json.dump(new_data, f)

def _update_main_data(key, value):
    c_data = get_main_data()
    c_data[key] = value
    _save_main_data(c_data)

def _append_to_main_data(key,append_value):
    c_data = get_main_data()
    if key not in c_data:
        c_data[key] = [append_value]
    else:
        c_data[key].append(append_value)
    _save_main_data(c_data)

def _get_from_main_data(key):
    c_data = get_main_data()
    if key in c_data: return c_data[key]
    return None


def get_main_data():
    global main_data
    if main_data:
        return main_data

    with open("data.json",'r') as f:
        main_data = json.loads(f.read())

    return main_data