from enum import Enum



class Language(Enum):
    GERMAN = "de"
    ENGLISH = "en"

current_language = Language.GERMAN
#current_language = Language.ENGLISH

def get_text(prompt_key, language):
    if language == Language.GERMAN:
        return prompt_key
    de_en = {
        'Hallo': 'Hello'
    }
    if language == Language.ENGLISH:
        return de_en[prompt_key]

print(get_text('Hallo', current_language))