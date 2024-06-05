from kivy.lang import Builder

from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.segmentedbutton import (
    MDSegmentedButton,
    MDSegmentedButtonItem,
    MDSegmentButtonLabel,
)
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDBoxLayout:
        id: box
        orientation: "vertical"
        size_hint_x: .7
        adaptive_height: True
        spacing: "24dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):
    def on_start(self):
        for segment_type in ["large", "normal", "medium", "small"]:
            self.root.ids.box.add_widget(
                MDBoxLayout(
                    MDLabel(
                        text=f"Type '{segment_type}'",
                        adaptive_height=True,
                        bold=True,
                        pos_hint={"center_y": 0.5},
                        halign="center",
                    ),
                    MDSegmentedButton(
                        MDSegmentedButtonItem(
                            MDSegmentButtonLabel(
                                text="Songs",
                            ),
                        ),
                        MDSegmentedButtonItem(
                            MDSegmentButtonLabel(
                                text="Albums",
                            ),
                        ),
                        MDSegmentedButtonItem(
                            MDSegmentButtonLabel(
                                text="Podcasts",
                            ),
                        ),
                        type=segment_type,
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    adaptive_height=True,
                )
            )

    def build(self):
        return Builder.load_string(KV)


Example().run()