from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem

KV = '''
MDScreen:
    GridLayout:
        cols: 3
        spacing: '0dp'
        padding: '0dp'
        size_hint_x: None
        size_hint_y: None
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        #labels
        MDLabel:
            text: 'Day'
            font_size: '14sp'
            size_hint_min_x: 120
            theme_text_color: 'Secondary'
        
        MDLabel:
            text: 'Month'
            font_size: '14sp'
            size_hint_min_x: 120
            theme_text_color: 'Secondary'
        
        MDLabel:   
            text: 'Year'
            font_size: '14sp'
            size_hint_min_x: 120
            theme_text_color: 'Secondary'

        MDFlatButton:
            id: day_button
            text: 'Day'
            font_size: '20sp'
            size_hint: None, None
            width: '120dp'
            height: '20dp'
            on_release: app.show_day_menu()
        
        MDFlatButton:
            id: month_button
            text: 'Month'
            font_size: '20sp'
            size_hint: None, None
            width: '120dp'
            height: '20dp'
            on_release: app.show_month_menu()

        FloatLayout:
            size_hint_x: None
            size_hint_y: None
            width: '120dp'
            height: '50dp'  # Adjust this value to change the height of the frame
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0  # invisible color
                Rectangle:
                    pos: self.pos
                    size: self.size
            MDTextField:
                hint_text: "Year"
                size_hint_x: None
                input_filter: 'int'
                pos_hint: {'center_x': 0.3, 'center_y': 0.43}
                font_size: '20sp'  # Same as the button font size
                on_focus: self.hint_text = '' if self.focus else 'Year' if self.text == '' else ''
                line_color_focus: 1, 0, 0, 0  # RGBA color for transparent
                line_color_normal: 1, 0, 0, 0  # RGBA color for transparent

'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_day_menu(self):
        days = [str(day) for day in range(1, 32)]
        menu_items = [{"viewclass": "OneLineListItem", "text": day, "on_release": lambda day=day: self.set_day({"text": day})} for day in days]
        self.day_menu = MDDropdownMenu(
            caller=self.root.ids.day_button,
            items=menu_items,
            position="auto"
        )
        self.day_menu.open()

    def show_month_menu(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        menu_items = [{"viewclass": "OneLineListItem", "text": month, "on_release": lambda month=month, month_number=months.index(month)+1: self.set_month({"text": month, "number": month_number})} for month in months]
        self.month_menu = MDDropdownMenu(
            caller=self.root.ids.month_button,
            items=menu_items,
            position="auto"
        )
        self.month_menu.open()
    
    def set_month(self, item):
        self.root.ids.month_button.text = item['text']
        print(f'Selected month: {item["text"]}, number: {item["number"]}')
        self.month_menu.dismiss()

    def set_day(self, item):
        self.root.ids.day_button.text = item['text']
        print(f'Selected day: {item["text"]}')
        self.day_menu.dismiss()

if __name__ == '__main__':
    MyApp().run()
