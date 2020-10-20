from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    Widget:
    canvas:
        Color:
            rgba: 0, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    MDFloatingActionButton:
        icon: "android"
        md_bg_color: app.theme_cls.primary_color
        margin: 10


'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()