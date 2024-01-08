from kivy.uix.screenmanager import Screen

class AddFamilyTreeScreen(Screen):
    def screen_method(self):
        print('Hello from addfamilytree')

    def checkFirstName(self, instance):
        # Only allow alphanumeric characters and dashes
        cleaned_text = ''
        print(instance.text)
        for ch in instance.text:
            if ch.isalpha() or ch == '-':
                cleaned_text += ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkSecondNames(self, instance):
        # Only allow alphanumeric characters, dashes, and spaces, no space-space, dash-space, space-dash, or dash-dash
        cleaned_text = ''
        previous_char = ''
        for i, ch in enumerate(instance.text):
            if i == 0 and (ch == '-' or ch == ' '):
                continue
            if ch.isalpha() or ch == '-' or ch == ' ':
                if ch == ' ' and previous_char == '-':
                    continue
                if ch == '-' and previous_char == ' ':
                    continue
                if ch == '-' and previous_char == '-':
                    continue
                if ch == ' ' and previous_char == ' ':
                    continue
                cleaned_text += ch
                previous_char = ch

        # Update the instance text with the cleaned text
        instance.text = cleaned_text

    def checkDashAtEnd(self, instance):
        # Check if the last character is a dash, if so, throw an error
        if instance.text[-1:] == '-':
            instance.error = True

    def checkLastName(self, instance):
        self.checkSecondNames(instance)
         
            


        

