from kivy.uix.screenmanager import Screen

class AddFamilyTreeScreen(Screen):
    def screen_method(self):
        print('Hello from addfamilytree')

    def isalpha(self, instance):
        # Remove non-alphabetic characters from the text
        cleaned_text = ''
        for ch in instance.text:
            if ch.isalpha():
                cleaned_text += ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def isalpha(self, instance):
        # Remove non-alphabetic characters from the text
        cleaned_text = ''
        for ch in instance.text:
            if ch.isalpha():
                cleaned_text += ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

