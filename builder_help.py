import json
import builder_data

builder_path = r'C:\Users\user\PycharmProjects\project_builder'


def _load_template(data):
    template_path = builder_path +"/templates/"+data["template"]

    with open(template_path,'r') as f:
        template_data = json.loads(f.read())

    return template_data

def get_latest_project():

    main_data = builder_data.get_main_data()

    with open(builder_path + "/" + main_data["latest_project"], 'r') as f:
        data = json.loads(f.read())
    return data


def find_property_with_name(properties, name):
    for p in properties:
        if p['name'] == name:
            return p
    return None

def key_valid(dict, key):
    return dict and key in dict and dict[key]
