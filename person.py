import json

import helpmethods as hm
import custom_datatypes as cdt

class Person:
    def __init__(self):
        # None: keine Angabe
        self.id = None
        self.first_names = [] # name list
        self.second_names = []
        self.last_names = []  # e.g. maiden name, remarriage
        self.pen_names = [] # string list

        self.nationalities = [] # string list
        self.academic_degrees = []
        
        self.birth_date = None
        self.death_date = None # None, [day, month, year, bc?, hour, minute, second, microsecond, time_zone]
        # death_date to True when date is unknown
        self.deathdate_unknown = False
        self.birth_place = None
        self.death_place = None
        self.genders = []  # u/m/w/d

        self.religions = [] 

        self.relations = [] # list of relation ids
        self.mother = None
        self.father = None
        self.adopted_father = False  # if adopted
        self.adopted_mother = False

        self.godparents = []  # relation has id
        self.godchilds = [] # relation has id

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def print_everything(self):
        print(f'ID: {self.id}')
        print(f'Firstnames: {self.string_first_names()}')
        print(f'Secondnames: {self.string_second_names()}')
        print(f'Familynames: {self.string_last_names()}')
        print(f'Pen names: {self.string_pen_names()}')
        print(f'Academic degrees: {self.academic_degrees}')
        print(f'Relations: {self.relations}')
        print(f'Gender: {self.string_genders()}')
        print(f'Birthdate: {self.birth_date}')
        print(f'Deathdate: {self.death_date}')
        print(f'Deathdate unknown: {self.deathdate_unknown}')
        print(f'Birthplace: {self.birth_place}')
        print(f'Deathplace: {self.death_place}')
        print(f'Religions: {self.religions}')
        print(f'Mother: {self.mother}')
        print(f'Father: {self.father}')
        print(f'Adopted father: {self.adopted_father}')
        print(f'Adopted mother: {self.adopted_mother}')
        print(f'Godparents1: {self.godparents}')
        print(f'Godchilds: {self.godchilds}')

    def add_firstname(self, text):
        if text != '':
            string_list = hm.remove_dash_return_list(text)
            name = hm.string_list_to_name(string_list)
            self.first_names.append(name)

    def add_secondname(self, text):
        if text != '':
            string_list = hm.remove_dash_return_list(text)
            name = hm.string_list_to_name(string_list)
            self.second_names.append(name)

    def add_secondnames(self, text):
        if text != '':
            string_list = hm.remove_space_return_list(text) # [Hans, Hans-Peter]
            for string in string_list:
                self.add_secondname(string)

    def add_lastname(self, text):
        if text != '':
            string_list = hm.remove_dash_return_list(text)
            name = hm.string_list_to_name(string_list)
            self.last_names.append(name)

    def add_lastnames(self, text):
        if text != '':
            string_list = hm.remove_space_return_list(text)
            for string in string_list:
                self.add_lastname(string)

    def add_pen_name(self, text):
        if text != '':
            self.pen_names.append(text)

    def add_academic_degree(self, text):
        pass

    def add_relation(self, relation):
        pass

    def add_gender(self, gender_num):
        gender = cdt.Gender()
        gender.gen = gender_num
        self.genders.append(gender)

    def add_birth_date(self, date_list):
        self.birth_date = date_list
    
    def add_death_date(self, date_list):
        self.death_date = date_list
    
    def add_deathdate_unknown(self, boolean):
        self.deathdate_unknown = boolean

    def add_birth_place(self, place):
        self.birth_place = place

    def add_death_place(self, place):
        self.death_place = place

    # return string function
    def string_first_names(self):
        out = ''
        for name in self.first_names:
            for part in name.name_components:
                out += part.component
                if part != name.name_components[-1]:
                    out += '-'
            if name != self.first_names[-1]:
                out += ', '
        return out
    
    def string_second_names(self):
        out = ''
        for name in self.second_names:
            for part in name.name_components:
                out += part.component
                if part != name.name_components[-1]:
                    out += '-'
            if name != self.second_names[-1]:
                out += ' '
        return out
    
    def string_last_names(self):
        out = ''
        for name in self.second_names:
            for part in name.name_components:
                out += part.component
                if part != name.name_components[-1]:
                    out += '-'
            if name != self.second_names[-1]:
                out += ' '
        return out
    
    def string_pen_names(self):
        return ', '.join(self.pen_names)
    
    def string_genders(self):
        return ', '.join([str(gender.gen) for gender in self.genders])
        

    

    


            



        


