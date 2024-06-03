from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (400, 600)

KV = '''
BoxLayout:
    id: main_layout
    orientation: 'vertical'

    MDSegmentedControl:
        id: segment_control
        size_hint_x: 1
        
        MDSegmentedControlItem:
            text: "Option 1"
        MDSegmentedControlItem:
            text: "Option 2"
        MDSegmentedControlItem:
            text: "Option 3"

    Button:
        text: "Get active button"
        on_release: app.get_active_button()
'''

class ExampleApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        Window.bind(on_resize=self.on_window_resized)
        return self.root

    def on_window_resized(self, window, width, height):
        # Get the size of the parent layout
        parent_width = width
        parent_width_dp = dp(parent_width/2)
        print(f"Parent layout width: {parent_width} pixels, {parent_width_dp} dp")

        # Access the segmented control and set its width
        self.root.ids.segment_control.ids.segment_panel.width = parent_width_dp

    def get_active_button(self):
        print("Get active button pressed")

if __name__ == "__main__":
    ExampleApp().run()
