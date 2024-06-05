import custom_datatypes as cdt
from datetime import datetime

def remove_dash_return_list(text):
    return text.split("-")

def string_list_to_name(list):
    name = cdt.Name()
    for component in list:
        name_component = cdt.Name_component()
        name_component.component = component
        name.name_components.append(name_component)
    return name

def remove_space_return_list(text):
    return text.split()
    