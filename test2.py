from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

# Set window size
Window.size = (400, 600)

KV = '''
MDScreen:
    MDFloatLayout:
        MDLabel:
            text: "Segment Control Example"
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .8}
        
        MDSegmentedControl:
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint: 0.8, None  # Adjusting the width to 80% of the parent and height to None
            #height: 48  # Specifying the height in dp (density-independent pixels)
            #segment_panel_height: "100dp"

            MDSegmentedControlItem:
                text: "1"
                width: dp(50)
            MDSegmentedControlItem:
                text: "2"
                width: dp(50)
            MDSegmentedControlItem:
                text: "3"
                width: dp(50)
            MDSegmentedControlItem:
                text: "4"
                width: dp(50)
            

'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def on_segment(self, instance_segment):
        print(f"Segment {instance_segment.text} selected")

if __name__ == '__main__':
    MainApp().run()
