from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.segmentedcontrol import MDSegmentedControl
from kivy.core.window import Window

Window.size = (500, 700)

KV = '''
BoxLayout:
    id: main_layout
    orientation: 'vertical'
    #padding: dp(20)
    #spacing: dp(20)

    MDSegmentedControl:
        id: segment_control
        size_hint_x: None
        width: dp(root.ids.segment_control.parent.size[0]/2)
        
        MDSegmentedControlItem:
            text: "Option 1"
        MDSegmentedControlItem:
            text: "Option 2"
        MDSegmentedControlItem:
            text: "Option 3"

    Button:
        text: "Get active button"
        on_release: app.on_start()
'''

class ExampleApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        # Get the size of the parent layout
        parent_size = self.root.ids.segment_control.parent.size
        print(f"Parent layout size: {parent_size}, {dp(parent_size[0]/2)}dp")

        # Access the segmented control and set its width
        #self.root.ids.segment_control.ids.segment_panel.width = dp(parent_size[0])
        self.root.ids.segment_control.ids.segment_panel.width = dp(parent_size[0]/2)

if __name__ == "__main__":
    ExampleApp().run()
