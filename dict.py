from enum import Enum

class Language(Enum):
    GERMAN = "de"
    ENGLISH = "en"

class dict:
    current_language = Language.GERMAN
    def set_Language(self, lang):
        self.current_language = lang

    def get_text(self, prompt_key):
        if self.current_language == Language.GERMAN:
            return prompt_key
        de_en = {
            'Amtlicher Vorname: ': 'Official First Name: ',
            'n': 'n',
            'j': 'y',
            'Name korrekt?: ': 'Name correct?: ',
            '(J/n)': '(Y/n)',
            'Name erneut eingeben: ': 'Enter name again: '
        }
        if self.current_language == Language.ENGLISH:
            return de_en[prompt_key]

