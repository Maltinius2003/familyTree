from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.pickers import MDDatePicker
from kivy.lang import Builder

KV = '''
MDScreen:
    MDFlatButton:
        text: "Open Date Picker"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.show_date_picker()
'''

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Optional: set the primary theme color
        return Builder.load_string(KV)

    def show_date_picker(self):
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_date_save, on_cancel=self.on_date_cancel)
        date_picker.open()

    def on_date_save(self, instance, value, date_range):
        """
        Handles the event when the user selects a date and confirms.
        :param instance: the instance of the MDDatePicker.
        :param value: the selected date.
        :param date_range: not used here, but can be if you implement a range picker.
        """
        print(f'Selected date: {value}')
        # Further processing can be done here (e.g., updating a label or storing the date)

    def on_date_cancel(self, instance, value):
        """
        Handles the event when the user cancels the date picker.
        """
        print('Date picking was canceled.')

if __name__ == '__main__':
    MyApp().run()