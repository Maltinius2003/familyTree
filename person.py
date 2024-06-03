import helpmethods as hm
import custom_datatypes as cdt

class Person:
    def __init__(self):
        # None: keine Angabe
        self.id = None
        self.first_names = [] # name list
        self.second_names = []
        self.last_names = []  # z.B. Geburtsname, Wiederheirat
        self.pen_names = [] # string list

        self.academic_degrees = []

        self.relations = [] # list of relation ids

        self.genders = []  # m/w/d
        self.birth_date = None
        self.death_date = None # None, [day, month, year, bc?, hour, minute, second, microsecond, time_zone]
        # death_date to True when date is unknown
        self.birth_place = None
        self.death_place = None

        self.religions = [] 

        self.mother = None
        self.father = None
        self.adopted_father = False  # Wenn von Vater adoptiert
        self.adopted_mother = False

        self.godparents1 = []  # z.B. Pate Taufe //Wenn nicht in Stammbaum neue Person erstellen (möglichst mit niemandem Verwandt)
        self.godparents2 = []  # z.B. Pate Firmung/Konfirmation
        self.godchilds = [] # id der Relation

    def print_everything(self):
        print(f'ID: {self.id}')
        print(f'Firstnames: {self.first_names}')
        print(f'Secondnames: {self.second_names}')
        print(f'Familynames: {self.last_names}')
        print(f'Pen names: {self.pen_names}')
        print(f'Academic degrees: {self.academic_degrees}')
        print(f'Relations: {self.relations}')
        print(f'Gender: {self.genders}')
        print(f'Birthdate: {self.birth_date}')
        print(f'Deathdate: {self.death_date}')
        print(f'Birthplace: {self.birth_place}')
        print(f'Deathplace: {self.death_place}')
        print(f'Religions: {self.religions}')
        print(f'Mother: {self.mother}')
        print(f'Father: {self.father}')
        print(f'Adopted father: {self.adopted_father}')
        print(f'Adopted mother: {self.adopted_mother}')
        print(f'Godparents1: {self.godparents1}')
        print(f'Godparents2: {self.godparents2}')
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

    def add_gender(self, letter):
        char_gen = letter.lower()
        gender = cdt.Gender()
        if char_gen == 'u':
            gender.gen = 0
        elif char_gen == 'm':
            gender.gen = 1
        elif char_gen == 'f':
            gender.gen = 2
        elif char_gen == 'd':
            gender.gen = 3
        self.genders.append(gender)

    def add_birth_date(self, date_list):
        self.birth_date = date_list
    
    def add_death_date(self, date_list):
        self.death_date = date_list
        # death_date to True when date is unknown

    def add_birth_place(self, place):
        self.birth_place = place

    def add_death_place(self, place):
        self.death_place = place

    

    


            



        


